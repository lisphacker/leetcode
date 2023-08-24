from typing import List

class Solution:
    def __init__(self):
        self.d1_to_e = {
            0: '',
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
        }
        self.d10_to_e = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety',
        }
        self.d11_to_e = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
        }
        self.level_to_english = {
            0: '',
            1: 'Thousand',
            2: 'Million',
            3: 'Billion'
        }
    def two_dig_to_english(self, num):
        d10 = num // 10
        d1 = num % 10

        # print(d10, d1, self.d10_to_e, self.d1_to_e)
        if d10 == 0:
            return self.d1_to_e[d1]
        elif num >= 10 and num <= 19:
            return self.d11_to_e[num]
        else:
            return self.d10_to_e[d10] + ('' if d1 == 0 else (' ' + self.d1_to_e[d1]))

    def three_dig_to_english(self, num):
        d100 = num // 100
        rest = num % 100
        s = '' if d100 == 0 else (self.d1_to_e[d100] + ' Hundred')
        s += ' ' + self.two_dig_to_english(rest)
        return s

    def numrec(self, num: int, level: int) -> str:
        last_three = num % 1000
        rest = num // 1000

        eng = '' if rest == 0 else self.numrec(rest, level + 1)
        if last_three != 0:
            eng += ' ' + self.three_dig_to_english(last_three) + ' ' + self.level_to_english[level]

        return eng

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        eng = self.numrec(num, 0)
        return ' '.join(eng.split())

import unittest

class Tests(unittest.TestCase):
    def compare(self, input, ref_output):
        self.assertEqual(ref_output, Solution().numberToWords(input))

    def test_1(self):
        self.compare(123, 'One Hundred Twenty Three')

    def test_2(self):
        self.compare(12345, 'Twelve Thousand Three Hundred Forty Five')

    def test_3(self):
        self.compare(1234567, 'One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven')

    def test_4(self):
        self.compare(1234567891, 'One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One')

    def test_5(self):
        self.compare(0, 'Zero')

    def test_6(self):
        self.compare(1000010, 'One Million Ten')

    def test_7(self):
        self.compare(100, 'One Hundred')

if __name__ == '__main__':
    unittest.main()
