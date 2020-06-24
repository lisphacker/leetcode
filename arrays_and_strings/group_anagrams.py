from typing import List
from itertools import groupby
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return []

        sorted_strs = list(map(lambda s: ''.join(sorted(s)), strs))
        indices = list(range(len(strs)))
        sorted_indices = sorted(indices, key=lambda v: sorted_strs[v])
        groups = []
        group = [strs[sorted_indices[0]]]
        sorted_str = sorted_strs[sorted_indices[0]]

        for i in sorted_indices[1:]:
            if sorted_strs[i] == sorted_str:
                group.append(strs[i])
            else:
                groups.append(group)
                group = [strs[i]]
                sorted_str = sorted_strs[i]

        groups.append(group)
        print(strs, groups)
        return groups

import unittest

class Tests(unittest.TestCase):
    def compare(self, input, ref_output):
        output = Solution().groupAnagrams(input)
        self.assertEqual(len(ref_output), len(output), 'Comparing output length')
        for r, o in zip(ref_output, output):
            self.assertListEqual(r, o, 'Comparing sublists')

    def test_1(self):
        self.compare(["eat", "tea", "tan", "ate", "nat", "bat"], 
            [
                ["ate","eat","tea"],
                ["nat","tan"],
                ["bat"]
            ])

if __name__ == '__main__':
    unittest.main()
