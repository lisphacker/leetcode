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
    def check_node(self, graph, partitions, visited, i):
        if i not in visited:
            return False

        p = visited[i]

        for j in graph[i]:
            if j in visited and visited[j] == p:
                return False

        return True

    def add_node(self, graph, partitions, visited, i):
        if i in visited:
            return self.check_node(graph, partitions, visited, i)

        for p in range(len(partitions)):
            visited[i] = p
            partitions[p].add(i)

            failed = False
            for j in graph[i]:
                if not self.add_node(graph, partitions, visited, j):
                    log(f'Failed to add {j}, neighbour to {i}')
                    log(graph, label='GRAPH')
                    log(partitions, label='PARTITONS')
                    log(visited, label='VISITED')
                    failed = True
                if failed:
                    break

            del visited[i]
            partitions[p].remove(i)

            if failed:
                return False

        return True

    def isBipartite(self, graph_data: List[List[int]]) -> bool:
        graph = {i:set(jj) for i, jj in enumerate(graph_data)}

        partitions = [set(), set()]
        visited = dict()

        for i in graph:
            if not self.add_node(graph, partitions, visited, i):
                return False

        return True

DEBUG = True

import unittest

class Tests(unittest.TestCase):
    def compare(self, input, ref_output):
        self.assertEqual(ref_output, Solution().isBipartite(input))

    def test_1(self):
        self.compare([[1,3],[0,2],[1,3],[0,2]], True)

    def test_2(self):
        self.compare([[1,2,3], [0,2], [0,1,3], [0,2]], False)

if __name__ == '__main__':
    unittest.main()
