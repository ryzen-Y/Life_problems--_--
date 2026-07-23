from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False


# == == == == == == == == = Improved == == == == == == == == ==


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        a = set(nums)
        if len(a) == len(nums):
            return False
        return True
