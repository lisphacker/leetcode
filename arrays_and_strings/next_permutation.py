from typing import List
from functools import reduce

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return

        i = len(nums) - 1

        while True:
            i -= 1
            if i < 0:
                nums.sort()
                return
            thisv = nums[i]
            bigger_exists = reduce(lambda r, x: r or (x > thisv), nums[i + 1:], False)
            if bigger_exists:
                subset = sorted(nums[i + 1:])
                nextv = None
                for j, v in enumerate(subset):
                    if v > thisv:
                        nextv = v
                        break

                subset[j] = thisv
                nums[i] = nextv
                nums[i + 1:] = sorted(subset)
                return
            else:
                pass


import unittest

class Tests(unittest.TestCase):
    def compare(self, input, ref_output):
        # print('Input:', input)
        # print('Ref output:', ref_output)
        Solution().nextPermutation(input)
        self.assertListEqual(ref_output, input)

    def test_1(self):
        self.compare([1, 2, 3], [1, 3, 2])

    def test_2(self):
        self.compare([3, 2, 1], [1, 2, 3])

    def test_3(self):
        self.compare([1, 1, 5], [1, 5, 1])

    def test_4(self):
        self.compare([1, 3, 2], [2, 1, 3])

    def test_5(self):
        self.compare([2, 3, 1], [3, 1, 2])

if __name__ == '__main__':
    unittest.main()
