from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        file = {}

        for i in range(len(nums)):
            if nums[i] in file:
                if i - file[nums[i]] <= k:
                    return True
            file[nums[i]] = i
        return False
