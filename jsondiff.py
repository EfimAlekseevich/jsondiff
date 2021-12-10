import pprint
import json
import sys

s = 'src'
c = 'cmp'


def get_json(filename: str):
    """Read json file to dict"""
    with open(filename) as f:
        return json.load(f)


def diff_lists(src: list, cmp: list):
    """Recursive comparing list elements"""
    global c, s
    i = 0
    diff_dict = {s: {}, c: {}}
    while i < len(src):
        if i < len(cmp):
            if src[i] == cmp[i]:
                pass
            elif isinstance(src[i], dict) and isinstance(cmp[i], dict):
                diff_dict[i] = diff_dicts(src[i], cmp[i])
            elif isinstance(src[i], list) and isinstance(cmp[i], list):
                diff_dict[i] = diff_lists(src[i], cmp[i])
            else:
                diff_dict[i] = {s: src[i], c: cmp[i]}
        else:
            diff_dict[i] = {s: src[i]}
        i += 1

    while i < len(cmp):
        diff_dict[i] = {c: cmp[i]}
        i += 1

    return diff_dict


def diff_dicts(src: dict, cmp: dict):
    """Recursive comparing key:value pairs"""
    global c, s
    diff_dict = {s: {}, c: {}}
    for key, value in src.copy().items():
        if key in cmp:
            if src[key] == cmp[key]:
                src.pop(key)
                cmp.pop(key)
            elif isinstance(src[key], dict) and isinstance(cmp[key], dict):
                diff_dict[key] = diff_dicts(src.pop(key), cmp.pop(key))
            elif isinstance(src[key], list) and isinstance(cmp[key], list):
                diff_dict[key] = diff_lists(src.pop(key), cmp.pop(key))
            else:
                diff_dict.update({key: {s: src.pop(key), c: cmp.pop(key)}})
        else:
            diff_dict[s].update({key: src.pop(key)})

    diff_dict[c] = cmp
    return diff_dict


def main():
    # global c, s
    # s = sys.argv[1]
    # c = sys.argv[2]
    source = [get_json(sys.argv[1])]
    compared = [get_json(sys.argv[2])]
    pprint.pprint(diff_lists(source, compared)[0])


if __name__ == '__main__':
    main()
