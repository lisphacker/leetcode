from typing import List
from pprint import pprint

DEBUG = False

def log(o, label=None, *args, **kwargs):
    if DEBUG:
        if label is not None:
            print(label)
            pprint(o)
            print()
        else:
            print(o, *args, **kwargs)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 0 and len(p) == 0:
            return True

        if len(s) == 0 or len(p) == 0:
            return False
        
        s0 = s[0]
        p0 = p[0]
        star = False if len(p) == 1 else (p[1] == '*')
        
        if not star:
            if p0 == '.':
                return self.isMatch(s[1:], p[1:])
            else:
                if s0 == p0:
                    return self.isMatch(s[1:], p[1:])
                else:
                    return False
        else:
            if p0 == '.':
                sr = s
                while True:
                    if self.isMatch(sr[1:], p):
                        return True
                    elif self.isMatch(sr, p[2:]):
                        return True
                    elif self.isMatch(sr[1:], p[2:]):
                        return True
                    sr = sr[1:]
                    if len(sr) == 0:
                        break
                return False
            else:
                sr = s
                while True:
                    if sr[0] == p0:
                        if self.isMatch(sr[1:], p):
                            return True
                        elif self.isMatch(sr[1:], p[2:]):
                            return True
                    else:
                        if self.isMatch(sr, p[2:]):
                            return True
                        else:
                            return False

                    sr = sr[1:]
                    if len(sr) == 0:
                        break

                return False
        return False

stest = 'ippi'
import unittest

class Tests(unittest.TestCase):
    def compare(self, input1,  input2, ref_output):
        self.assertEqual(ref_output, Solution().isMatch(input1, input2))

    def test_1(self):
        self.compare('aa', 'a', False)

    def test_2(self):
        self.compare('aa', 'a*', True)

    def test_3(self):
        self.compare('ab', '.*', True)

    def test_4(self):
        self.compare('aab', 'c*a*b*', True)

    def test_5(self):
        self.compare('mississippi', 'mis*is*p*.', False)

    def test_6(self):
        self.compare('a', 'ab*.', True)

if __name__ == '__main__':
    unittest.main()
