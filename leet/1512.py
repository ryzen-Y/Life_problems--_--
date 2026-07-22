from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in nums[i+1:]:
                if nums[i] == j:
                    count += 1
        return count
