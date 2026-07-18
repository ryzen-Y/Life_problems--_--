from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        out = []
        for i in nums:
            count = 0
            for j in nums:
                if i > j:
                    count += 1
            out.append(count)

        return out
