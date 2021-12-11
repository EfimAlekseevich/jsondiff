import pprint
import json
from argv_parser import define_designations, parse_argv


s, c = 'src', 'cmp'


def get_json(filename: str):
    """Read json file to dict"""
    with open(filename) as f:
        return json.load(f)


def save_result(filename: str, extension: str, result):
    with open(f'{filename}.{extension}', 'w') as f:
        if extension == 'json':
            json.dump(result, f)
        else:
            f.write(result)


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

    # Preparing
    global c, s
    args = parse_argv()
    s, c = define_designations(args)

    source = [get_json(args.source_filename)]
    compared = [get_json(args.compared_filename)]

    # Processing
    result = diff_lists(source, compared)[0]

    # Output
    result_filename = 'result' if not args.result_filename else args.result_filename
    if args.text:
        save_result(result_filename, 'txt', pprint.pformat(result))
    if args.json:
        save_result(result_filename, 'json', result)

    pprint.pprint(result)


if __name__ == '__main__':
    main()
