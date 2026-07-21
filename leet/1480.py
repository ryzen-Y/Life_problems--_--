from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        ans = 0
        sum = []

        for i in nums:
            ans = ans + i
            sum.append(ans)
        return sum
