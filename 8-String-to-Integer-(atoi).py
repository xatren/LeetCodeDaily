class Solution(object):
    def myAtoi(self, s):
        \\\
        :type s: str
        :rtype: int
        \\\
        # ignore whitespace
        s = s.strip()
        
        if not s:
            return 0
        
        
        sign = 1
        index = 0
        if s[0] in ['-', '+']:
            sign = -1 if s[0] == '-' else 1
            index += 1
        
        
        result = 0
        while index < len(s) and s[index].isdigit():
            result = result * 10 + int(s[index])
            index += 1
        
        # sign
        result *= sign
        
        # overflow
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result