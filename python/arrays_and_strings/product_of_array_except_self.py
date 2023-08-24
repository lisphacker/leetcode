from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [0] * len(nums)

        zero_pos = -1
        zero_count = 0
        p = 1
        for i, n in enumerate(nums):
            if n == 0:
                zero_pos = i
                zero_count += 1
            if n != 0:
                p *= n
                out[i] = p

        if zero_count > 1:
            for i in range(len(out)):
                out[i] = 0
            return out

        p = 1
        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]

            l = 1 if i == 0 else out[i - 1]
            r = 1 if i == len(nums) - 1 else p
 
            # print(i, out, l, r)
            out[i] = l * r

            p *= n

        return out

import unittest

class Tests(unittest.TestCase):
    def compare(self, input, ref_output):
        self.assertListEqual(ref_output, Solution().productExceptSelf(input))

    def test_1(self):
        self.compare([1,2,3,4], [24,12,8,6])

    def test_2(self):
        self.compare([0, 0], [0, 0])

    def test_3(self):
        self.compare([0, 4, 0], [0, 0, 0])

if __name__ == '__main__':
    unittest.main()
