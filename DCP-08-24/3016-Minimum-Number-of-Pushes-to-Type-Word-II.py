class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        frequency = Counter(word)
        
        sorted_frequencies = sorted(frequency.values(), reverse=True)
        
        total_pushes = 0
        
        press_count = 1
        
        for i, freq in enumerate(sorted_frequencies):
            if i != 0 and i % 8 == 0:
                press_count += 1
            total_pushes += freq * press_count
        
        return total_pushes