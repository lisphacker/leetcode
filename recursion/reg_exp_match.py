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
    def __init__(self):
        self.cache = dict()

    def isMatch(self, s: str, p: str) -> bool:
        if (s, p) in self.cache:
            return self.cache[(s, p)]
        log(f'isMatch({s}, {p})')

        if len(s) == 0 and len(p) == 0:
            return True

        star = False if len(p) < 2 else (p[1] == '*')
        
        if not star:
            if len(p) == 0 or len(s) == 0:
                self.cache[(s, p)] = False
                return False
            if p[0] == '.':
                return self.isMatch(s[1:], p[1:])
            else:
                if s[0] == p[0]:
                    return self.isMatch(s[1:], p[1:])
                else:
                    self.cache[(s, p)] = False
                    return False
        else:
            if p[0] == '.':
                if len(s) > 0 and self.isMatch(s[1:], p):
                    return True
                elif len(s) > 0 and self.isMatch(s[1:], p[2:]):
                    self.cache[(s, p)] = True
                    return True
                elif self.isMatch(s, p[2:]):
                    self.cache[(s, p)] = True
                    return True
                else:
                    self.cache[(s, p)] = False
                    return False
            else:
                if len(s) > 0:
                    if s[0] == p[0]:
                        if self.isMatch(s[1:], p):
                            self.cache[(s, p)] = True
                            return True
                        elif self.isMatch(s[1:], p[2:]):
                            self.cache[(s, p)] = True
                            return True
                        elif self.isMatch(s, p[2:]):
                            self.cache[(s, p)] = True
                            return True
                        else:
                            self.cache[(s, p)] = False
                            return False
                    else:
                        if self.isMatch(s, p[2:]):
                            self.cache[(s, p)] = True
                            return True
                        else:
                            self.cache[(s, p)] = False
                            return False
                else:
                    if self.isMatch(s, p[2:]):
                        self.cache[(s, p)] = True
                        return True
                    else:
                        self.cache[(s, p)] = False
                        return False

        self.cache[(s, p)] = False
        return False

DEBUG = False

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
        self.compare('a', 'ab*', True)

    def test_7(self):
        self.compare('bbbba', '.*a*a', True)

    def test_8(self):
        n = 10
        input = 'a' * n + 'b'
        output = 'a*' * n + 'c'
        self.compare(input, output, False)

    def test_9(self):
        self.compare('aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*c', False)

if __name__ == '__main__':
    unittest.main()
