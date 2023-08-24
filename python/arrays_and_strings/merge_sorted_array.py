from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        o = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[o] = nums1[p1]
                o -= 1
                p1 -= 1
            else:
                nums1[o] = nums2[p2]
                o -= 1
                p2 -= 1

        while p1 >= 0:
            nums1[o] = nums1[p1]
            o -= 1
            p1 -= 1

        while p2 >= 0:
            nums1[o] = nums2[p2]
            o -= 1
            p2 -= 1




import unittest

class Tests(unittest.TestCase):
    def compare(self, input1, len1, input2, len2, ref_output):
        Solution().merge(input1, len1, input2, len2)
        self.assertEqual(ref_output, input1)

    def test_1(self):
        self.compare([1,2,3,0,0,0], 3, [2,5,6], 3, [1,2,2,3,5,6])

if __name__ == '__main__':
    unittest.main()
