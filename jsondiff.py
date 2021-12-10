"""
Create application that will find the difference between two input JSON files.

Requirements:
- Solve the core algorithm problem at hand. What data structure do you need to use? What's the asymptotic upper bound of the algorithm?
- Design the output format.
- Clear documentation about how to run the program (README.md file).

Artifacts:
Link to repository on GitHub that contains: source code, README.md

Technology requirements:
no any limitations

Input:
two JSON files
Format example:
<app> <pathtofile1> <pathtofile2>

Output:
the difference between two JSON files

Examples:
File-A.json
{
"firstName": "John",
"lastName": "Smith",
"isAlive": true,
"age": 27,
"address": {
"streetAddress": "21 2nd Street",
"city": "New York",
"state": "NY",
"postalCode": "10021-3100"
}
}
File-B.json
{
"first_name": "Alex",
"lastName": "Smith",
"isAlive": false,
"Age": 27,
"address": {
"streetAddress": "21 2nd Street",
"city": "Chicago",
"state": "IL"
}
}

Conditions:

The answers are only accepted as a link to the repository(s) with the solutions.
Share your test results with our Tech Team by sending the link to the repository to rnd_lab@itrexgroup.com
You have 5 days to complete the test.

Easy path:
$ pip install jsondiff
# from jsondiff import diff
# from pprint import pprint
# if __name__ == '__main__':
#     pprint(diff(FileA, FileB))

Idea:

Diff types:

- key exist only in source (source, src)
- key exist only in compared (compared, cmp)
- different values of the same key (diff, *key)

"""

import json
import sys


def main():
    # source_filename = sys.argv[1]
    # compared_filename = sys.argv[2]
    #
    # source = get_json(source_filename)
    # compared = get_json(compared_filename)
    from examples import FileA, FileB

    source = FileA
    compared = FileB
    import pprint
    pprint.pprint(diff_dict(source, compared))


def diff_dict(src: dict, cmp: dict, depth=0):
    diff_dct = {}
    for key, value in src.copy().items():
        if key not in cmp:  # source
            print(0, key, depth)
            if 'src' in diff_dct:
                diff_dct['src'].update({key: src.pop(key)})
            else:
                diff_dct.update({'src': {key: src.pop(key)}})
        elif value != cmp[key]:  # diff
            if isinstance(value, dict) and isinstance(cmp[key], dict):
                print(1, key, depth)
                diff_dct.update({key: diff_dict(src.pop(key), cmp.pop(key), depth+1)})
            else:
                print(2, key, depth)
                diff_dct.update({key: {'src': src.pop(key), 'cmp': cmp.pop(key)}})
        else:  # remove checked pair
            print(3, key, depth)
            src.pop(key)
            cmp.pop(key)

        diff_dct.update({'cmp': cmp.copy()})  # compared

    return diff_dct


def get_json(filename):
    with open(filename) as f:
        return json.load(f)


if __name__ == '__main__':
    main()

