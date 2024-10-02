class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        sorted_unique = sorted(set(arr))
        
        rank_map = {num: rank + 1 for rank, num in enumerate(sorted_unique)}
        
        return [rank_map[num] for num in arr]