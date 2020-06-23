from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        wi = 1
        ri = 1
        c = nums[0]
        l = len(nums)
        while ri < l:
            while ri < l and nums[ri] == c:
                ri += 1
            if ri == l:
                break
            nums[wi] = nums[ri]
            c = nums[ri]
            wi += 1
            ri += 1

        return wi

import unittest

class Tests(unittest.TestCase):
    def run_test(self, input, ref_output):
        self.assertEqual(Solution().removeDuplicates(input), ref_output)

    def test_1(self):
        self.run_test([1, 1, 2], 2)

    def test_2(self):
        self.run_test([0,0,1,1,1,2,2,3,3,4], 5)

if __name__ == '__main__':
    unittest.main()