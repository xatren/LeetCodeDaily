class Solution(object):
    def findKthNumber(self, n, k):
        \\\
        :type n: int
        :type k: int
        :rtype: int
        \\\
        def count_prefix(prefix, n):
            curr = prefix
            next_prefix = prefix + 1
            count = 0
            while curr <= n:
                count += min(n + 1, next_prefix) - curr
                curr *= 10
                next_prefix *= 10
            return count

        current = 1
        k -= 1  

        while k > 0:
            count = count_prefix(current, n)
            if k >= count:
                k -= count
                current += 1
            else:
                current *= 10
                k -= 1

        return current