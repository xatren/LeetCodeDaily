class Solution(object):
    def shortestPalindrome(self, s):
        \\\
        :type s: str
        :rtype: str
        \\\
        if not s:
            return \\
        
        temp = s + '#' + s[::-1]
        
        table = [0] * len(temp)
        
        for i in range(1, len(temp)):
            j = table[i - 1]
            while j > 0 and temp[i] != temp[j]:
                j = table[j - 1]
            table[i] = j + (temp[i] == temp[j])
        
        # The length of the longest palindrome
        longest_prefix = table[-1]
        
        # Add the remaining characters in reverse order
        return s[longest_prefix:][::-1] + s