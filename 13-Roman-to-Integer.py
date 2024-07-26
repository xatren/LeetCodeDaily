class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Mapping of Roman numerals to integers
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0

        # Iterate over the string in reverse
        for char in reversed(s):
            value = roman_to_int[char]
            
            # If the current value is less than the previous value, subtract it
            if value < prev_value:
                total -= value
            else:
                total += value
            
            # Update previous value
            prev_value = value
        
        return total
