class Solution(object):
    def checkInclusion(self, s1, s2):
        \\\
        :type s1: str
        :type s2: str
        :rtype: bool
        \\\
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

        # Count the frequencies of characters in s1
        for char in s1:
            s1_count[ord(char) - ord('a')] += 1

        # Initialize the window
        for i in range(len(s1)):
            window_count[ord(s2[i]) - ord('a')] += 1

        if s1_count == window_count:
            return True

        # Slide the window
        for i in range(len(s1), len(s2)):
            # Remove the first character of the previous window
            window_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
            # Add the current character to the window
            window_count[ord(s2[i]) - ord('a')] += 1

            if s1_count == window_count:
                return True

        return False