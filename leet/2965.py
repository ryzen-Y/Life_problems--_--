from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        total = n*n
        freq = [0] * (total+1)

        for row in grid:
            for num in row:
                freq[num] += 1

        repeat = missing = 0

        for num in range(1, total+1):
            if freq[num] == 2:
                repeat = num
            elif freq[num] == 0:
                missing = num

        return [repeat, missing]
