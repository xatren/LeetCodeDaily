from collections import Counter

class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        # Combine words from both sentences
        words = s1.split() + s2.split()
        
        # Count occurrences of each word
        word_counts = Counter(words)
        
        # Return words that appear exactly once
        return [word for word, count in word_counts.items() if count == 1]