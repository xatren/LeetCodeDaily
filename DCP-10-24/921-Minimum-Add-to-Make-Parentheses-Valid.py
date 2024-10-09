class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = 0  
        additions = 0  

        for char in s:
            if char == '(':
                stack += 1
            elif char == ')':
                if stack > 0:
                    stack -= 1
                else:
                    additions += 1

        additions += stack

        return additions