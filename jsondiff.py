import pprint
import json
import sys


def get_json(filename):
    with open(filename) as f:
        return json.load(f)


def diff(src: dict, cmp: dict):
    diff_dct = {'src': {}, 'cmp': {}}
    for key, value in src.copy().items():
        if key not in cmp:
            diff_dct['src'].update({key: src.pop(key)})
        elif value != cmp[key]:
            diff_dct.update({key: diff(src.pop(key), cmp.pop(key))} if
                            isinstance(value, dict) and isinstance(cmp[key], dict) else
                            {key: {'src': src.pop(key), 'cmp': cmp.pop(key)}})
        else:
            src.pop(key)
            cmp.pop(key)
    diff_dct.update({'cmp': cmp.copy()})

    return diff_dct


def main():
    source = get_json(sys.argv[1])
    compared = get_json(sys.argv[2])
    pprint.pprint(diff(source, compared))


if __name__ == '__main__':
    main()
