symval = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

class Solution:
    def romanToInt(self, s: str) -> int:
        stack = []

        value = 0
        for c in s:
            v = symval[c]
            if len(stack) == 0 or stack[-1] < v:
                if len(stack) != 0:
                    stack.append(-stack.pop())
                stack.append(v)
            else:
                while len(stack) != 0:
                    value += stack.pop()
                stack.append(v)
        
        while len(stack) != 0:
            value += stack.pop()

        return value

import unittest

class UnitTests(unittest.TestCase):
    def check(self, roman: str, val: int):
        self.assertEqual(Solution().romanToInt(roman), val)

    def test_3(self):
        self.check('III', 3)

    def test_4(self):
        self.check('IV', 4)

    def test_9(self):
        self.check('IX', 9)

    def test_58(self):
        self.check('LVIII', 58)

    def test_1994(self):
        self.check('MCMXCIV', 1994)

if __name__ == '__main__':
    unittest.main()