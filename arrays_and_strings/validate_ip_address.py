from typing import List

class Solution:
    def validate_ipv4(self, IP: str) -> str:
        parts = IP.split('.')
        if len(parts) != 4:
            return 'Neither'
        
        for part in parts:
            if len(part) == 0:
                return 'Neither'
            if part == '0':
                continue
            if part[0] == '0':
                return 'Neither'
            for c in part:
                if not c.isdigit():
                    return 'Neither'
            n = int(part)
            if n < 0 or n > 255:
                return 'Neither'
        return 'IPv4'                    
    
    def validate_ipv6(self, IP: str) -> str:
        parts = IP.split(':')
        if len(parts) != 8:
            return 'Neither'

        for part in parts:
            if len(part) == 0 or len(part) > 4:
                return 'Neither'
            for c in part:
                if not c.isdigit() and c not in 'abcdefABCDEF':
                    return 'Neither'

        return 'IPv6'
    
    def validIPAddress(self, IP: str) -> str:
        if IP.find('.') >= 0:
            return self.validate_ipv4(IP)
        else:
            return self.validate_ipv6(IP)

import unittest

class Tests(unittest.TestCase):
    def compare(self, input, ref_output):
        self.assertEqual(ref_output, Solution().validIPAddress(input))

    def test_1(self):
        self.compare('172.16.254.1', 'IPv4')

    def test_2(self):
        self.compare('2001:0db8:85a3:0:0:8A2E:0370:7334', 'IPv6')

    def test_3(self):
        self.compare('256.256.256.256', 'Neither')

    def test_4(self):
        self.compare('01.01.01.01', 'Neither')

    def test_5(self):
        self.compare('2001:0db8:85a3:00000:0:8A2E:0370:7334', 'Neither')

    def test_6(self):
        self.compare('192.0.0.1', 'IPv4')

    def test_7(self):
        self.compare('172.16.254.10', 'IPv4')

if __name__ == '__main__':
    unittest.main()
