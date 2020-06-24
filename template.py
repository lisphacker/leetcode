import unittest

class Solution:
    def apply(self, input):
        pass

class Tests(unittest.TestCase):
    def compare(self, input, ref_output):
        self.assertEqual(ref_output, Solution().apply(input))

    def test_1(self):
        self.compare('2', '3', '6')

    def test_2(self):
        self.compare('123', '456', '56088')

if __name__ == '__main__':
    unittest.main()
