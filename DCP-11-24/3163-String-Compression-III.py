class Solution(object):
    def compressedString(self, word):
        """
        :type word: str
        :rtype: str
        """
        comp = []  
        i = 0
        n = len(word)
        
        while i < n:
            count = 1
            while i + 1 < n and word[i] == word[i + 1] and count < 9:
                count += 1
                i += 1
            
            comp.append("{}{}".format(count, word[i]))
            
            i += 1
        
        return ''.join(comp)  