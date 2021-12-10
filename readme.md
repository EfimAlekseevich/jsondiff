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

### Examples:
see examples.py


## Easy path:
`$ pip install jsondiff `
```
from jsondiff import diff
from pprint import pprint

if __name__ == '__main__':
    pprint(diff(file_a, file_b))
```
## Idea:

### Diff types:

- key exist only in source (source, src)
- key exist only in compared (compared, cmp)
- different values of the same key (diff, *key)

### Questions, cases:
- handling incorrect json (few identical keys)
- case sensitivity in keys, strings
- the order of the elements in the array
- what goal this task?
    - help fix differences in json files?
    - show differences between files?

### Output design:
#### Problems
- identical keys ("src" and "cmp")


### Algorithm:
See on json-file as on list of pairs key: value.