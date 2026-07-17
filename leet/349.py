from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        common = []
        for i in nums1:
            for j in nums2:
                if i == j and i not in common:
                    common.append(i)

        return common
