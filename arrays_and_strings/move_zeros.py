from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        ri = wi = 0
        while ri < len(nums):
            while ri < len(nums) and nums[ri] == 0:
                ri += 1
            if ri == len(nums):
                break
            nums[wi] = nums[ri]
            wi += 1
            ri += 1

        for i in range(wi, len(nums)):
            nums[i] = 0

import unittest

class Tests(unittest.TestCase):
    def compare(self, input, ref_output):
        Solution().moveZeroes(input)
        self.assertListEqual(ref_output, input)

    def test_1(self):
        self.compare([0,1,0,3,12], [1,3,12,0,0])

if __name__ == '__main__':
    unittest.main()
