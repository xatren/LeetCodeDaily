class Solution(object):
    def isPalindrome(self, s):
        \\\
        :type s: str
        :rtype: bool
        \\\
        # clear chars
        cleaned_chars = []
        for char in s:
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9':
                cleaned_chars.append(char.lower())
        
        cleaned_s = \\.join(cleaned_chars)
        
        # control palindrome
        left = 0
        right = len(cleaned_s) - 1
        
        while left < right:
            if cleaned_s[left] != cleaned_s[right]:
                return False
            left += 1
            right -= 1
            
        return True