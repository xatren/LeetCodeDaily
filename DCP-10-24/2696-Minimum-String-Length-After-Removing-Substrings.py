class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for char in s:
            if stack:
                if (stack[-1] == 'A' and char == 'B') or (stack[-1] == 'C' and char == 'D'):
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        
        return len(stack)