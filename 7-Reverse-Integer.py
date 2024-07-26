class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # Define the 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Determine the sign of the number
        sign = -1 if x < 0 else 1
        x *= sign  # Work with positive numbers
        
        # Reverse the digits of the integer
        reversed_x = 0
        while x != 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10
        
        # Restore the sign
        reversed_x *= sign
        
        # Check for overflow
        if reversed_x < INT_MIN or reversed_x > INT_MAX:
            return 0
        
        return reversed_x
