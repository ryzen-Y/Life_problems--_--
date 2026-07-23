from collections import Counter
from collections import Couters


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = sorted(s)
        b = sorted(t)

        if a == b:
            return True
        return False


# ========== counter =========


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)
