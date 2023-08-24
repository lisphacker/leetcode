from typing import List
from functools import reduce

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if s == '':
            return 0

        p0 = 0
        p1 = 0

        r0 = 0
        r1 = -1

        counts = dict()
        counts[s[p0]] = 1

        while p0 <= p1:
            unique_count = reduce(lambda acc, v: acc + (1 if v > 0 else 0), counts.values(), 0)
            # print((p0, p1), (r0, r1), unique_count, counts)
            if unique_count <= k:
                if r1 - r0 < p1 - p0:
                    r0, r1 = p0, p1
            if unique_count > k or p1 == len(s) - 1:
                c = s[p0]
                if c in counts:
                    counts[c] -= 1
                p0 += 1
            else:
                p1 += 1
                c = s[p1]
                if c in counts:
                    counts[c] += 1
                else:
                    counts[c] = 1

        return r1 - r0 + 1


import unittest

class Tests(unittest.TestCase):
    def compare(self, input1,  input2, ref_output):
        self.assertEqual(ref_output, Solution().lengthOfLongestSubstringKDistinct(input1, input2))

    def test_1(self):
        self.compare('eceba', 2, 3)

    def test_2(self):
        self.compare('aa', 1, 2)

    def test_3(self):
        self.compare('a', 0, 0)

if __name__ == '__main__':
    unittest.main()
