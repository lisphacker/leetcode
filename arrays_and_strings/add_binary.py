from typing import Tuple

class Solution:
    def add_bits(self, b0: int, b1: int, carry: int) -> Tuple[int, int]:
        out = b0 + b1 + carry
        carry = 1 if out > 1 else 0
        out = out % 2
        return out, carry

    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = '0' * (len(a) - len(b)) + b
        else:
            a = '0' * (len(b) - len(a)) + a

        bits = []
        carry = 0
        for bs0, bs1 in zip(reversed(a), reversed(b)):
            b0 = 0 if bs0 == '0' else 1
            b1 = 0 if bs1 == '0' else 1
            o, carry = self.add_bits(b0, b1, carry)
            bits.append(str(o))
        bits.append(str(carry))

        out = ''.join(reversed(bits))
        while len(out) > 1 and out[0] == '0':
            out = out[1:]
        if len(out) == 0:
            out = '0'
        return out

import unittest

class Tests(unittest.TestCase):
    def compare(self, input1, input2, ref_output):
        self.assertEqual(ref_output, Solution().addBinary(input1, input2))

    def test_1(self):
        self.compare('11', '1', '100')

    def test_2(self):
        self.compare('1010', '1011', '10101')

if __name__ == '__main__':
    unittest.main()
