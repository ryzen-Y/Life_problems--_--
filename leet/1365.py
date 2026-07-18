from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        t = sorted(nums)
        ans = []
        dic = {}

        for i, val in enumerate(t):
            if val not in dic:
                dic[val] = i

        for i in nums:
            ans.append(dic[i])
        return ans
