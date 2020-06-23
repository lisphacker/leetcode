from typing import List

class Solution:
    def swap(self, nums: List[int], i: int, j: int) -> None:
        t = nums[i]
        nums[i] = nums[j]
        nums[j] = t

    def rec(self, nums: List[int], i: int) -> None:
        if i < 0:
            last = nums[-1]
            for j in range(len(nums) - 1, 0, -1):
                nums[j] = nums[j - 1]
            nums[0] = last
            return

        if nums[i] < nums[i + 1]:
            self.swap(nums, i, i + 1)
        else:
            self.swap(nums, i, i + 1)
            self.rec(nums, i - 1)

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return

        i = len(nums) - 2

        self.rec(nums, i)

import unittest

class Tests(unittest.TestCase):
    def compare(self, input, ref_output):
        print('Input:', input)
        print('Ref output:', ref_output)
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
