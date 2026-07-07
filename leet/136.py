class Solution(object):
    def singleNumber(self, nums):

        count = {}

        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        for _ in count:
            if count[_] == 1:
                return _
