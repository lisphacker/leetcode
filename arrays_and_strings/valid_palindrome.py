from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1
        
        if s == '':
            return True

        while i < len(s) and not s[i].isalnum():
            i += 1
            
        while j >= 0 and not s[j].isalnum():
            j -= 1
        
        if i > j:
            return True

        while i <= j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

            while i < len(s) and not s[i].isalnum():
                i += 1
                
            while j >= 0 and not s[j].isalnum():
                j -= 1
            
        return True

import unittest

class Tests(unittest.TestCase):
    def compare(self, input, ref_output):
        self.assertEqual(ref_output, Solution().isPalindrome(input))

    def test_1(self):
        self.compare('A man, a plan, a canal: Panama', True)

    def test_2(self):
        self.compare('race a car', False)

    def test_3(self):
        self.compare(' ', True)

if __name__ == '__main__':
    unittest.main()
