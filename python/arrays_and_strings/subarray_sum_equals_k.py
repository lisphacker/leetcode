from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return 0

        count = 0
        s = 0
        m = {0: 1}
        for n in nums:
            # print('>>>', n, count, s, m)
            s += n
            if s - k in m:
                count += m[s - k]
            m[s] = m.get(s, 0) + 1
            # print('<<<', n, count, s, m)
        return count

import unittest

class Tests(unittest.TestCase):
    def compare(self, input1,  input2, ref_output):
        self.assertEqual(ref_output, Solution().subarraySum(input1, input2))

    def test_1(self):
        self.compare([1,1,1], 2, 2)

    def test_2(self):
        self.compare([100,1,2,3,4], 6, 1)

    def test_3(self):
        self.compare([28,54,7,-70,22,65,-6], 100, 1)

    def test_4(self):
        self.compare(list(range(10000)), 33, 4)

if __name__ == '__main__':
    unittest.main()
