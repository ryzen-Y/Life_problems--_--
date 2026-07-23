class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        flag = False
        for i in range(len(nums)):
            if nums[i] in nums[i+1:]:
                flag = True

        return flag
