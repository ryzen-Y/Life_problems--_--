from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct = sorted(set(nums))

        if len(distinct) < 3:
            return distinct[-1]
        return distinct[-3]
