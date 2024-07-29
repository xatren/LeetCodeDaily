class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        while "AB" in s or "CD" in s:
            s = s.replace("AB", "")
            s = s.replace("CD", "")
        return len(s)
