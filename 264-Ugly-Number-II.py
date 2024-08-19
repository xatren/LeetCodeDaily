class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [0] * n
        ugly[0] = 1
        i2 = i3 = i5 = 0
        next2, next3, next5 = 2, 3, 5
        
        for i in range(1, n):
            next_ugly = min(next2, next3, next5)
            ugly[i] = next_ugly
            
            if next_ugly == next2:
                i2 += 1
                next2 = ugly[i2] * 2
            if next_ugly == next3:
                i3 += 1
                next3 = ugly[i3] * 3
            if next_ugly == next5:
                i5 += 1
                next5 = ugly[i5] * 5
                
        return ugly[-1]