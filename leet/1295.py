from typinng import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        digits = 0

        for i in nums:
            digits = 0
            while i > 0:
                i = i // 10
                digits += 1

            if digits % 2 == 0:
                count += 1
        return count
