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
            print(o, *args, **kwargs)

class Solution:
    def reduce_adjacent_ranges(self, ranges):
        n = len(ranges)
        
        while len(ranges) > 1:
            change_detected = False
            i = 0
            while i < len(ranges) - 1:
                if ranges[i][1] + 1 == ranges[i + 1][0]:
                    ranges[i][1] = ranges[i + 1][1]
                    del ranges[i + 1]
                    change_detected = True
                else:
                    i += 1
                    
            if not change_detected:
                break
        return n != len(ranges)
    
    def reduce_nested_ranges(self, ranges, s):
        n = len(ranges)
        cd = False
        while True:
            change_detected = False
            for i, (j, k) in enumerate(ranges):
                if j > 0 and k < len(s) - 1:
                    if s[j - 1] == '(' and s[k + 1] == ')':
                        ranges[i] = [j - 1, k + 1]
                        change_detected = True
            cd = cd or change_detected    
            if not change_detected:
                break
                
        return cd
    
    def longestValidParentheses(self, s: str) -> int:
        ranges = []
        
        for i in range(1, len(s)):
            if s[i - 1] == '(' and s[i] == ')':
                ranges.append([i - 1, i])

                
        while True:
            change_detected = False
            log((ranges, change_detected), label='111')
            cd = self.reduce_adjacent_ranges(ranges)
            change_detected = change_detected or cd
            log((ranges, change_detected), label='222')
            cd = self.reduce_nested_ranges(ranges, s)
            change_detected = change_detected or cd
            log((ranges, change_detected), label='333')
            if not change_detected:
                break
            
        mxl = None
        for i, j in ranges:
            l = j - i + 1
            if mxl is None or mxl < l:
                mxl = l
                
        return 0 if mxl is None else mxl

# DEBUG = True

import unittest

class Tests(unittest.TestCase):
    def compare(self, input, ref_output):
        self.assertEqual(ref_output, Solution().longestValidParentheses(input))

    def test_1(self):
        self.compare('(()', 2)

    def test_2(self):
        self.compare(')()())', 4)

    def test_3(self):
        self.compare(')(()()))', 6)

    def test_4(self):
        self.compare('()(())', 6)


if __name__ == '__main__':
    unittest.main()
