from typing import Tuple

class Solution:
    ORD0 = ord('0')

    def multiply_digits(self, digit1: int, digit2: int, carry: int) -> Tuple[int, int]:
        r = digit1 * digit2 + carry
        if r >= 10:
            carry = r // 10
            r = r % 10
        else:
            carry = 0
        return r, carry

    def multiply_with_digit(self, num: str, digit: int):
        carry = 0
        r = ''
        for i, d in enumerate(map(lambda c: ord(c) - Solution.ORD0, reversed(num))):
            d2, carry = self.multiply_digits(d, digit, carry)
            r = f'{d2}' + r
        if carry != 0:
            r = f'{carry}' + r
        return r

    def add_digits(self, digit1: int, digit2: int, carry: int) -> Tuple[int, int]:
        r = digit1 + digit2 + carry
        if r >= 10:
            carry = r // 10
            r = r % 10
        else:
            carry = 0
        return r, carry

    def add(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1 = '0' * (len(num2) - len(num1)) + num1
        else:
            num2 = '0' * (len(num1) - len(num2)) + num2
        
        r = ''
        carry = 0
        num1 = map(lambda c: ord(c) - Solution.ORD0, reversed(num1))
        num2 = map(lambda c: ord(c) - Solution.ORD0, reversed(num2))
        
        for d1, d2 in zip(num1, num2):
            d3, carry = self.add_digits(d1, d2, carry)
            r = f'{d3}' + r

        if carry != 0:
            r = f'{carry}' + r

        return r

    def multiply(self, num1: str, num2: str) -> str:
        acc = '0'
        for i, digit in enumerate(map(lambda c: ord(c) - Solution.ORD0, reversed(num2))):
            p = self.multiply_with_digit(num1, digit)
            p = p + '0' * i
            acc = self.add(acc, p)

        while len(acc) > 0:
            if acc[0] == '0':
                acc = acc[1:]
            else:
                break
        if acc == '':
            acc = '0'

        return acc

import unittest

class Tests(unittest.TestCase):
    def compare(self, input1, input2, ref_output):
        self.assertEqual(ref_output, Solution().multiply(input1, input2))

    def test_1(self):
        self.compare('2', '3', '6')

    def test_2(self):
        self.compare('123', '456', '56088')

    def test_3(self):
        self.compare('9', '9', '81')

if __name__ == '__main__':
    unittest.main()
