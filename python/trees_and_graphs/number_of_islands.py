from pprint import pprint

class Solution:
    def number_island(self, island_map: List[List[int]], x: int, y: int, num: int):
        island_map[y][x] = num
        if x > 0 and island_map[y][x - 1] == -1:
            self.number_island(island_map, x - 1, y, num)
        if x < len(island_map[y]) - 1 and island_map[y][x + 1] == -1:
            self.number_island(island_map, x + 1, y, num)
        if y > 0 and island_map[y - 1][x] == -1:
            self.number_island(island_map, x, y - 1, num)
        if y < len(island_map) - 1 and island_map[y + 1][x] == -1:
            self.number_island(island_map, x, y + 1, num)
            
        
    def find_islands(self, island_map: List[List[int]], num: int) -> int:
        found_unnumbered_node = False
        for y, row in enumerate(island_map):
            for x, v in enumerate(row):
                if v == -1:
                    found_unnumbered_node = True
                    # print('BEFORE', num, '\n', island_map)
                    self.number_island(island_map, x, y, num)
                    # print('AFTER', num, '\n', island_map)
                    break
            if found_unnumbered_node:
                break
        
        if found_unnumbered_node:
            return self.find_islands(island_map, num + 1)
        
        return num
    
    def numIslands(self, grid: List[List[str]]) -> int:
        island_map = []
        for row in grid:
            island_map.append(list(map(lambda x: 0 if x == '0' else -1, row)))
    
        r = self.find_islands(island_map, 1)
        
        pprint(grid)
        pprint(island_map)
        
        return r - 1
        
        