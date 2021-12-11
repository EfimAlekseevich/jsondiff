# Application that will find the difference between two JSON files.

### Requirements:
- Solve the core algorithm problem at hand. What data structure do you need to use? What's the asymptotic upper bound of the algorithm?
- Design the output format.
- Clear documentation about how to run the program (README.md file).

### Artifacts:
Link to repository on GitHub that contains: source code, README.md

### Technology requirements:
no any limitations

### Input:
two JSON files
Format example:
<app> <pathtofile1> <pathtofile2>

### Output:
the difference between two JSON files

## Easy path:
`$ pip install jsondiff `
```
from jsondiff import diff
from pprint import pprint

if __name__ == '__main__':
    pprint(diff(file_a, file_b))
```
## Core algorithm concepts:
### Q&A
What data structure do you need to use? - Non linear data structure -> Trees Data Structure -> dict
Why? - Json is Trees Data Structure
What's the asymptotic upper bound of the algorithm? -
### Diff types:
- key exist only in source (source, src)
- key exist only in compared (compared, cmp)
- different values of the same key (diff, *key)

### Questions, cases:
- handling of incorrect json (multiple identical keys) needed?
- is case sensitivity in keys, strings important when comparing?
- is the order of the items in the list important when comparing?
- error handling in case of incorrect use of the program needed?
- what is the purpose of this task?
    - help fix differences in json files?
    - show differences between files?

### Output design:

#### Dict differences:
```
{
'src': {key1: value1, key2: value2, ...}, # pairs only in source dict
'cmp': {key3: value3, key4: value4, ...}, # pairs only in source dict
'key5': {'src': value5, 'cmp': 'value6'} # pairs with identical key but different values
'key6': { pairs with identical key but different values with type list(or dict)
        'src': {key7: value7, key8: value8, ...}, # pairs only in source dict
        'cmp': {key3: value3, key4: value4, ...}, # pairs only in source dict
        'key5': {'src': value5, 'cmp': 'value6'} # pairs with identical key but different values}
        'key7': {etc}
}
```

#### List differences:
```
{
'src': {3: value3, 4: value4, ...}, # elements only in source list (3,4 - indexes of elements in source list)
'cmp': {}, # empty because the src list is longer
0: {'src': 'value_s0', 'cmp': 'value_c0'} # elements with identical index but different values (0 - index)
1: { # elements with identical index but different values with type list(or dict)
        'src': {}, # empty because the cmp list is longer
        'cmp': {3: value_3, 4: value_4, ...}, # elements only in cmp list (3,4 - indexes of elements in source list)
        1: {'src': value_s1, 'cmp': 'value_c1'} # elements with identical index but different values
        2: {etc}
}
```

#### Problems
- identical keys ("src" and "cmp")
- keys as numbers (1, 2, 3) - JSON names require double quotes.

## Tutorial
```
usage: jsondiff.py [-h] [--source SOURCE] [--compared COMPARED] [--filenames] [--result_filename RESULT_FILENAME] [--text] [--json] source_filename compared_filename

It is program for comparing two json files

positional arguments:
  source_filename       filename of the source json file
  compared_filename     filename of the compared json file

optional arguments:
  -h, --help            show this help message and exit
  --source SOURCE, -s SOURCE
                        designation of the source file
  --compared COMPARED, -c COMPARED
                        designation of the compared file
  --filenames, -f       use filenames for designation of the files
  --result_filename RESULT_FILENAME, -r RESULT_FILENAME
                        name for result file
  --text, -t            save result to txt
  --json, -j            save result to json !integer keys will replaced strings (1 -> "1")!

```
