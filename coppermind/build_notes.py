import os
import sys
from collections import Counter
from hashlib import sha256

import yaml
import numpy as np

from tags import pull_tags


class Note:
    def __init__(self, text, tags, name):
        self.text = text
        self.tags = set(tags)
        self.name = name

    def __str__(self):
        return f"""
Note: {self.text}
Tags: {sorted(self.tags)}\n
From: {self.name}
        """

    def get_hash(self):
        return sha256((self.name + self.text).encode("utf-8")).hexdigest()


def extract_tags(tags):
    tags = [tag.strip().lower() for tag in tags]
    # tags = [word.strip() for tag in tags for word in tag.split(" ")]
    return [tag for tag in tags if tag]


def parse_note(entry, context, name):
    return Note(
        entry["note"].strip(),
        extract_tags(entry.get("tags", [])) + context,
        name,
    )


def parse_notes(notes, context, name):
    for entry in notes:
        if "note" in entry:
            yield parse_note(entry, context, name)
        else:
            entry = entry[list(entry.keys())[0]]
            new_context = context + extract_tags(entry["tags"])
            notes = entry["notes"]
            for note in parse_notes(notes, new_context, name):
                yield note


def pick_node(notes, remaining):
    counter = Counter()
    for note in notes:
        counter.update([tag for tag in note.tags if tag in remaining])
    words = sorted(counter.keys())
    probs = np.array([counter[word] / len(notes) for word in words])
    entropy = -probs * np.log(probs)
    return words[np.argmax(entropy)], np.max(entropy)


def build_tree(tree, node, used, min_leaves):

    notes = tree[node]
    total_notes = len(notes)
    tree[node] = {}
    nodes = tree[node]

    remaining = set([tag for note in notes for tag in note.tags]) - used
    while remaining:
        new_node, _ = pick_node(notes, remaining)
        relevant_notes = [note for note in notes if new_node in note.tags]
        if (
            len(relevant_notes) < min_leaves
            or len(notes) - len(relevant_notes) < min_leaves
        ):
            break
        nodes[new_node] = relevant_notes
        notes = [note for note in notes if new_node not in note.tags]
        for note in nodes[new_node]:
            remaining -= note.tags
    if len(notes) == total_notes:
        tree[node] = notes
        return

    if len(notes) > 0:
        nodes["other"] = notes

    for node in nodes.keys():
        build_tree(nodes, node, set([node]) | used, min_leaves)


def render_tree(tree, level):
    content = ""
    for key, value in tree.items():
        content += "#" * level + " " + key.capitalize() + "\n"
        if isinstance(value, dict):
            content += render_tree(value, level + 1)
        else:
            for note in value:
                content += ">" + note.text + "\n\n"
                content += "-" + note.name + "\n"
                content += note.get_hash() + "\n\n"
    return content


def add_tags(note, tags):
    new_tags = set(note.tags)
    for tag in note.tags:
        if tag not in tags:
            yield tag
        else:
            new_tags.update(tags[tag])
    note.tags = new_tags


def add_tags_full(notes, tags):
    bad_tags = set()
    for note in notes:
        for bad_tag in add_tags(note, tags):
            bad_tags.add(bad_tag)
    assert not bad_tags, f"Missing from tags: {sorted(bad_tags)}"


if __name__ == "__main__":

    query_tags = set([tag.strip().lower() for tag in sys.argv[1].split(",")])
    tags = pull_tags()

    missing = query_tags - set(tags)
    assert not missing, f"Tags queried but not found: {sorted(missing)}"

    notes = []
    for file in os.listdir("./notes"):
        if file.endswith(".yaml"):
            with open("./notes/" + file, "r") as file:
                data = yaml.safe_load(file)
            notes.extend(list(parse_notes(data["notes"], [], data["name"])))
    print(len(notes))

    add_tags_full(notes, tags)

    notes = [note for note in notes if set(note.tags) & query_tags == query_tags]
    print(len(notes))

    tree = {"my notes": notes}
    build_tree(tree, "my notes", set(), 3)

    with open("notes.md", "w") as fh:
        fh.write(render_tree(tree, 1))
