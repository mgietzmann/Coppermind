import os
import json


def flatten_tags_def(array, tags_def):
    if array:
        yield array
    for key, val in tags_def.items():
        if not val:
            yield [key] + array
        elif not isinstance(val, dict):
            yield [key] + array
        else:
            for x in flatten_tags_def([key] + array, tags_def[key]):
                yield x


def pull_tags():
    tags = {}
    for file in os.listdir("tags"):
        with open(f"tags/{file}", "r") as fh:
            tags_def = json.load(fh)
        for flattened in flatten_tags_def([], tags_def):
            flattened = [t.lower() for t in flattened]
            key = flattened[0]
            assert key not in tags, f"{key} is used more than once!"
            tags[key] = flattened[1:]
    return tags


if __name__ == "__main__":
    for key, array in pull_tags().items():
        print(key, array)
