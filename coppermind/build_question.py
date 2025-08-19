import os
import sys

import yaml

from build_notes import parse_notes


PROMPT = """
Hello! I have a markdown file with headers that are questions (subheaders being sub questions) 
and content that is notes taken from a series of papers (text then a citation). Starting with 
the lowest level questions and working your way up can you summarize the answer to each question 
using only the notes given (and the answers you come up with given those notes)? Please format 
it under the same headers as the input document. Thanks!
"""


def lookup_note(_hash, notes):
    return next(note for note in notes if note.get_hash() == _hash)


def render_question(data, notes, depth):
    if depth == 1:
        content = PROMPT + "\n\n"
    else:
        content = ""

    question = data["question"]
    content += "#" * depth + " " + f"{question}".capitalize() + "\n\n"
    for item in data["answer"]:
        if isinstance(item, dict):
            content += render_question(item, notes, depth + 1)
        else:
            note = lookup_note(item, notes)
            content += note.text + "\n\n"
            content += note.name + "\n\n"
    return content


if __name__ == "__main__":
    notes = []
    for file in os.listdir("./notes"):
        if file.endswith(".yaml"):
            with open("./notes/" + file, "r") as file:
                data = yaml.safe_load(file)
            notes.extend(list(parse_notes(data["notes"], [], data["name"])))
    print(len(notes))

    question_file = sys.argv[1]
    with open(question_file, "r") as file:
        data = yaml.safe_load(file)

    with open("question.md", "w") as file:
        file.write(render_question(data, notes, 1))
