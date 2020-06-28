from typing import List

class Solution:
    def validate(self, s: str, count: int) -> bool:
        i = 0
        j = len(s) - 1

        while i <= j and s[i] == s[j]:
            i += 1
            j -= 1
        if i > j:
            return True

        r1 = False
        if s[i + 1] == s[j]:
            if count > 0:
                return False
            r1 = self.validate(s[i + 1:j + 1], count + 1)

        r2 = False
        if s[i] == s[j - 1]:
            if count > 0:
                return False
            r2 = self.validate(s[i:j], count + 1)

        return r1 or r2

    def validPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True

        return self.validate(s, 0)


import unittest

class Tests(unittest.TestCase):
    def compare(self, input, ref_output):
        self.assertEqual(ref_output, Solution().validPalindrome(input))

    def test_1(self):
        self.compare('aba', True)

    def test_2(self):
        self.compare('abca', True)

    def test_3(self):
        self.compare("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga", True)

if __name__ == '__main__':
    unittest.main()
