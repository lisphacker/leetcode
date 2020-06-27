from typing import List

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t:
            return False
            
        si = ti = 0

        diff_found = False
        while si < len(s) and ti < len(t):
            # print(111, si, ti)
            if s[si] == t[ti]:
                si += 1
                ti += 1
                continue

            if si + 1 < len(s) and s[si + 1] == t[ti]:
                if diff_found:
                    return False
                else:
                    diff_found = True
                    si += 2
                    ti += 1
            elif ti + 1 < len(t) and s[si] == t[ti + 1]:
                if diff_found:
                    return False
                else:
                    diff_found = True
                    si += 1
                    ti += 2
            else:
                if diff_found:
                    return False
                else:
                    diff_found = True
                    si += 1
                    ti += 1
        
        s = abs((len(s) - si) - (len(t) - ti))
        # print(si, ti, s)

        if diff_found:
            if s > 0:
                return False
        else:
            if s > 1:
                return False

        return True

import unittest

class Tests(unittest.TestCase):
    def compare(self, input1,  input2, ref_output):
        self.assertEqual(ref_output, Solution().isOneEditDistance(input1, input2))

    def test_1(self):
        self.compare('ab', 'acb', True)

    def test_2(self):
        self.compare('cab', 'ad', False)

    def test_3(self):
        self.compare('1203', '1213', True)

if __name__ == '__main__':
    unittest.main()
