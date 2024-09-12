class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed_set = set(allowed)
        consistent_count = 0
        
        for word in words:
            if all(char in allowed_set for char in word):
                consistent_count += 1
        
        return consistent_count
