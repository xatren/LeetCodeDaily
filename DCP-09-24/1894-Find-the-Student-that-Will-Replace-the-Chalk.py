class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        total_sum = sum(chalk)
        k = k % total_sum

        for i in range(len(chalk)):
            if k < chalk[i]: 
                return i
            k -= chalk[i]