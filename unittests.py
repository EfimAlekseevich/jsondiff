import unittest
from jsondiff import diff_lists, diff_dicts, c, s


class TestListDiff(unittest.TestCase):

    def test_empty_empty(self):
        src = []
        cmp = []
        self.assertEqual(diff_lists(src, cmp), {c: {}, s: {}})

    def test_empty_filled(self):
        src = []
        cmp = [1, 2, 3]
        self.assertEqual(diff_lists(src, cmp), {s: {}, c: {},
                                                0: {c: 1},
                                                1: {c: 2},
                                                2: {c: 3}})

    def test_filled_empty(self):
        src = [1, 2, 3]
        cmp = []
        self.assertEqual(diff_lists(src, cmp), {s: {}, c: {},
                                                0: {s: 1},
                                                1: {s: 2},
                                                2: {s: 3}})

    def test_lists_empty(self):
        src = [[], [], []]
        cmp = []
        self.assertEqual(diff_lists(src, cmp), {s: {}, c: {},
                                                0: {s: []},
                                                1: {s: []},
                                                2: {s: []}})

    def test_lists_lists(self):
        src = [[], [], []]
        cmp = [[], [], []]
        self.assertEqual(diff_lists(src, cmp), {s: {}, c: {}})

    def test_empty_lists(self):
        src = []
        cmp = [[], [], []]
        self.assertEqual(diff_lists(src, cmp), {s: {}, c: {},
                                                0: {c: []},
                                                1: {c: []},
                                                2: {c: []}})

    def test_case_insensitive_str(self):
        src = ['aBcDEfg']
        cmp = ['abCDefG']
        self.assertEqual(diff_lists(src, cmp, cs_str=True), {s: {}, c: {}})


class TestDictDiff(unittest.TestCase):

    def test_empty_empty(self):
        src = {}
        cmp = {}
        self.assertEqual(diff_dicts(src, cmp), {c: {}, s: {}})

    def test_empty_filled(self):
        src = {}
        cmp = {'1': 2}
        self.assertEqual(diff_dicts(src, cmp), {s: {}, c: {'1': 2}})

    def test_filled_empty(self):
        src = {'1': 2}
        cmp = {}
        self.assertEqual(diff_dicts(src, cmp), {s: {'1': 2}, c: {}})

    def test_lists_empty(self):
        src = {'1': {}, '2': {}}
        cmp = {}
        self.assertEqual(diff_dicts(src, cmp), {s: {'1': {}, '2': {}}, c: {}})

    def test_lists_lists(self):
        src = {'1': {}, '2': {}}
        cmp = {'2': {}, '1': {}}
        self.assertEqual(diff_dicts(src, cmp), {s: {}, c: {}})

    def test_empty_lists(self):
        src = {}
        cmp = {'1': {}, '2': {}}
        self.assertEqual(diff_dicts(src, cmp), {c: {'1': {}, '2': {}}, s: {}})

    def test_case_insensitive_key_1(self):
        src = {'a': 1}
        cmp = {'A': 1}
        self.assertEqual(diff_dicts(src, cmp, True), {s: {}, c: {}})

    def test_case_insensitive_key_2(self):
        src = {'A': 1}
        cmp = {'a': 1}
        self.assertEqual(diff_dicts(src, cmp, True), {s: {}, c: {}})

    def test_case_insensitive_key_3(self):
        src = {'a': 1}
        cmp = {'A': 2}
        self.assertEqual(diff_dicts(src, cmp, True), {s: {}, c: {},
                                                      'a': {s: 1, c: 2}})

    def test_case_insensitive_key_4(self):
        src = {'A': 1}
        cmp = {'a': 2}
        self.assertEqual(diff_dicts(src, cmp, True), {s: {}, c: {},
                                                      'A': {s: 1, c: 2}})

    def test_case_insensitive_str(self):
        src = {'a': 'aBcDEfg'}
        cmp = {'a': 'abCDefG'}
        self.assertEqual(diff_dicts(src, cmp, cs_str=True), {s: {}, c: {}})

    def test_case_insensitive_str_key(self):
        src = {'A': 'aBcDEfg', 'b': 'aBcDEfg'}
        cmp = {'a': 'abCDefG', 'B': 'abcDefg'}
        self.assertEqual(diff_dicts(src, cmp, True, True), {s: {}, c: {}})


class TestDictListDiff(unittest.TestCase):

    def test_wrappers_diff_types(self):
        src = [{1: []}]
        cmp = [{1: {}}]
        self.assertEqual(diff_lists(src, cmp), {s: {}, c: {},
                                                0: {s: {}, c: {},
                                                    1: {s: [], c: {}}}})

    def test_wrappers_depth_3(self):
        src = [1, {'1': [2]}]
        cmp = [2, {'1': [1]}]
        self.assertEqual(diff_lists(src, cmp), {s: {}, c: {},
                                                0: {s: 1, c: 2},
                                                1: {s: {}, c: {},
                                                    '1': {s: {}, c: {},
                                                          0: {s: 2, c: 1}}}})

    def test_case_insensitive_str_key(self):
        src = {'A': 'aBcDEfg', 'b': 'aBcDEfg', 'c': ['aB', 'Bc']}
        cmp = {'a': 'abCDefG', 'B': 'abcDefg', 'C': ['ab', 'BC']}
        self.assertEqual(diff_dicts(src, cmp, True, True), {s: {}, c: {},
                                                            'c': {c: {}, s: {}}})


class TestExamples(unittest.TestCase):

    def test_example_1(self):
        src = {
            "firstName": "John",
            "lastName": "Smith",
            "isAlive": True,
            "age": 27,
            "address": {
                "streetAddress": "21 2nd Street",
                "city": "New York",
                "state": "NY",
                "postalCode": "10021-3100"
            }
        }
        cmp = {
            "first_name": "Alex",
            "lastName": "Smith",
            "isAlive": False,
            "Age": 27,
            "address": {
                "streetAddress": "21 2nd Street",
                "city": "Chicago",
                "state": "IL"
            }
        }
        self.assertEqual(diff_lists([src], [cmp])[0], {c: {"first_name": "Alex", "Age": 27},
                                                       s: {"firstName": "John", "age": 27},
                                                       "isAlive": {c: False, s: True},
                                                       "address": {c: {},
                                                                   s: {"postalCode": "10021-3100"},
                                                                   "city": {c: "Chicago", s: "New York"},
                                                                   "state": {c: "IL", s: "NY"}}
                                                       })

    def test_example_1_case_insensitive_keys(self):
        src = {
            "firstName": "John",
            "lastName": "Smith",
            "isAlive": True,
            "age": 27,
            "address": {
                "streetAddress": "21 2nd Street",
                "city": "New York",
                "state": "NY",
                "postalCode": "10021-3100"
            }
        }
        cmp = {
            "first_name": "Alex",
            "lastName": "Smith",
            "isAlive": False,
            "Age": 27,
            "address": {
                "streetAddress": "21 2nd Street",
                "city": "Chicago",
                "state": "IL"
            }
        }
        self.assertEqual(diff_lists([src], [cmp], True)[0], {c: {"first_name": "Alex"},
                                                             s: {"firstName": "John"},
                                                             "isAlive": {c: False, s: True},
                                                             "address": {c: {},
                                                                         s: {"postalCode": "10021-3100"},
                                                                         "city": {c: "Chicago", s: "New York"},
                                                                         "state": {c: "IL", s: "NY"}}
                                                             })


if __name__ == '__main__':
    unittest.main()
