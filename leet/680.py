class Solution:
    def checking(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return self.checking(s, left + 1, right) or self.checking(s, left, right - 1)
            left += 1
            right -= 1
        return True
