MINVAL = -(2**31)
MAXVAL = 2**31 - 1

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        negative = False

        if len(s) == 0:
            return 0

        if s[0] in '-+':
            if s[0] == '-':
                negative = True
            s = s[1:]

        v = 0
        ord0 = ord('0')
        for c in s:
            if c in '0123456789':
                v = v * 10 + (ord(c) - ord0)
            else:
                break

        if negative:
            v = -v

        if v < MINVAL:
            v = MINVAL
        if v > MAXVAL:
            v = MAXVAL

        return v

import unittest

class Tests(unittest.TestCase):
    def run_test(self, s: str, i: int):
        return self.assertEqual(Solution().myAtoi(s), i)

    def test_simple(self):
        self.run_test('42', 42)

    def test_negative_with_preceding_spaces(self):
        self.run_test('   -42', -42)

    def test_number_with_succeeding_words(self):
        self.run_test('4193 with words', 4193)

    def test_number_with_preceding_words(self):
        self.run_test('words and 987', 0)

    def test_out_of_range(self):
        self.run_test('-91283472332', -2147483648)

if __name__ == '__main__':
    unittest.main()
