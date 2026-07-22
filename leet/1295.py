class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        digit_list = []

        for i in nums:
            digit_list = []
            while i > 0:
                digit = i % 10
                i = i // 10
                digit_list.append(digit)

            if len(digit_list) % 2 == 0:
                count += 1
        return count
