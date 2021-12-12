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


def lowercase_keys(dct: dict):
    """All keys are in the root of lowercase letters"""
    for key, value in dct.copy().items():
        del dct[key]
        dct[key.lower()] = value


def diff_lists(src: list, cmp: list, cs_key=False, cs_str=False):
    """Recursive comparing list elements"""
    global c, s
    diff_dict = {s: {}, c: {}}

    for i in range(len(src)):
        if i < len(cmp):
            if src[i] == cmp[i] or \
                    (cs_str and isinstance(src[i], str) and isinstance(cmp[i], str) and src[i].lower() == cmp[
                        i].lower()):
                continue
            elif isinstance(src[i], dict) and isinstance(cmp[i], dict):
                diff_dict[i] = diff_dicts(src[i], cmp[i], cs_key, cs_str)
            elif isinstance(src[i], list) and isinstance(cmp[i], list):
                diff_dict[i] = diff_lists(src[i], cmp[i], cs_key, cs_str)
            else:
                diff_dict[i] = {s: src[i], c: cmp[i]}
        else:
            diff_dict.update({j: {s: src[j]} for j in range(i, len(src))})
            break

    for j in range(len(src), len(cmp)):
        diff_dict[j] = {c: cmp[j]}

    return diff_dict


def diff_dicts(src: dict, cmp: dict, cs_key=False, cs_str=False):
    """Recursive comparing key:value pairs"""
    global c, s
    diff_dict = {s: {}, c: {}}
    if cs_key:
        lowercase_keys(cmp)

    for key, value in src.copy().items():
        if (not cs_key and key in cmp) or (cs_key and key.lower() in cmp):
            cmp_key = key.lower() if cs_key else key

            if src[key] == cmp[cmp_key] or (cs_str and isinstance(src[key], str) and isinstance(cmp[cmp_key], str) and
                                            src[key].lower() == cmp[cmp_key].lower()):
                src.pop(key)
                cmp.pop(cmp_key)
            elif isinstance(src[key], dict) and isinstance(cmp[cmp_key], dict):
                diff_dict[key] = diff_dicts(src.pop(key), cmp.pop(cmp_key), cs_key, cs_str)
            elif isinstance(src[key], list) and isinstance(cmp[key], list):
                diff_dict[key] = diff_lists(src.pop(key), cmp.pop(cmp_key), cs_key, cs_str)
            else:
                diff_dict.update({key: {s: src.pop(key), c: cmp.pop(cmp_key)}})
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
    result = diff_lists(source, compared, cs_key=args.cs_key_disable, cs_str=args.cs_str_disable)[0]

    # Output
    result_filename = 'result' if not args.result_filename else args.result_filename
    if args.text:
        save_result(result_filename, 'txt', pprint.pformat(result))
    if args.json:
        save_result(result_filename, 'json', result)
    pprint.pprint(result)


if __name__ == '__main__':
    main()
