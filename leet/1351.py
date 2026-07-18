from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        for _ in grid:
            for i in _:
                if i < 0:
                    count += 1

        return count
