class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        result = []
        counts = [('a', a), ('b', b), ('c', c)]
        
        while True:
            counts.sort(key=lambda x: x[1], reverse=True)
            
            for char, count in counts:
                if count == 0:
                    return ''.join(result)
                
                if len(result) >= 2 and result[-1] == result[-2] == char:
                    continue
                
                result.append(char)
                counts = [(c, n - (1 if c == char else 0)) for c, n in counts]
                break
            else:
                return ''.join(result)