from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        sum_here = n * (n+1) // 2
        actual_sum = sum(nums)

        return sum_here - actual_sum
