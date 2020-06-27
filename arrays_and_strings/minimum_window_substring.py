from typing import List
from functools import reduce

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = dict()
        req_counts = dict()
        for c in t:
            count[c] = 0
            if c in req_counts:
                req_counts[c] += 1
            else:
                req_counts[c] = 1

        p0 = 0
        p1 = 0

        r0 = 0
        r1 = -1

        c = s[p0]
        if c in count:
            count[c] += 1
        while p0 <= p1:
            all_present = reduce(lambda acc, c: acc and count[c] >= req_counts[c], count.keys(), True)
            #print(111, (p0, p1), s[p0:p1 + 1], (r0, r1), s[r0:r1+1], all_present, count, req_counts)
            if all_present:
                if p1 - p0 < r1 - r0 or r1 == -1:
                    r0, r1 = p0, p1
            if all_present or p1 == len(s) - 1:
                c = s[p0]
                if c in count:
                    count[c] -= 1
                p0 += 1
            else:
                p1 += 1
                c = s[p1]
                if c in count:
                    count[c] += 1

        #print('OUT', r0, r1, s[r0:(r1 + 1)])
        return '' if r1 == -1 else s[r0:(r1 + 1)]


import unittest

class Tests(unittest.TestCase):
    def compare(self, input1, input2, ref_output):
        self.assertEqual(ref_output, Solution().minWindow(input1, input2))

    def test_1(self):
        self.compare('ADOBECODEBANC', 'ABC', 'BANC')

    def test_2(self):
        self.compare('a', 'aa', '')

if __name__ == '__main__':
    unittest.main()
