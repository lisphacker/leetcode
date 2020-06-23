from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = set()
        for i, x in enumerate(nums):
            m = -x

            j = i + 1
            k = len(nums) - 1

            while j < k:
                y = nums[j]
                z = nums[k]

                yz = y + z
                if yz == m:
                    triplets.add((x, y, z))
                    j += 1
                    k -= 1
                elif yz < m:
                    j += 1
                else:
                    k -= 1

        return [[x, y, z] for (x, y, z) in triplets]

import unittest

class Tests(unittest.TestCase):
    def run_test(self, input, ref_output):
        test_output = Solution().threeSum(input)
        self.assertEqual(len(ref_output), len(test_output))
        for r, t in zip(ref_output, test_output):
            self.assertListEqual(r, t)

    def test_1(self):
        self.run_test([-1, 0, 1, 2, -1, -4],
            [
                [-1, 0, 1],
                [-1, -1, 2]
            ])

    def test_2(self):
        self.run_test([-2,0,1,1,2],
            [
                [-2,0,2],
                [-2,1,1]
            ])

if __name__ == '__main__':
    unittest.main()