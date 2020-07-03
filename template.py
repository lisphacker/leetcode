from typing import List
from pprint import pprint

DEBUG = False

def log(o, label=None, *args, **kwargs):
    if DEBUG:
        if label is not None:
            print(label)
            pprint(o)
            print()
        else:
            print(*args, **kwargs)

class Solution:
    def apply(self, input):
        pass

import unittest

class Tests(unittest.TestCase):
    def compare(self, input, ref_output):
        self.assertEqual(ref_output, Solution().apply(input))

    def test_1(self):
        self.compare('input', 'output')

    def compare(self, input1,  input2, ref_output):
        self.assertEqual(ref_output, Solution().apply(input1, input2))

    def test_1(self):
        self.compare('input1', 'input2', 'output')

if __name__ == '__main__':
    unittest.main()
