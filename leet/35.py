from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if target not in nums:
            for i in range(len(nums)):
                if nums[i] > target:
                    return i
            return len(nums)

        else:
            return nums.index(target)
