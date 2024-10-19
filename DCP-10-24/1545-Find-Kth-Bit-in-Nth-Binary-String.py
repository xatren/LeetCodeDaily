class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def generate_sn(n):
            if n == 1:
                return "0"
            prev = generate_sn(n - 1)
            inverted = ''.join('1' if bit == '0' else '0' for bit in prev)
            return prev + "1" + inverted[::-1]
        
        sn = generate_sn(n)
        return sn[k - 1]