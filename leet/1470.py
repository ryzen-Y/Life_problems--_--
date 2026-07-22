from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        num1 = nums[:n]
        num2 = nums[n:]
        ans = []
        for x, y in zip(num1, num2):
            ans.append(x)
            ans.append(y)
        return ans
