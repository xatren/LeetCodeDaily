import heapq

class Solution(object):
    def maxKelements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        score = 0
        
        for _ in range(k):
            val = -heapq.heappop(max_heap)
            score += val
            val_new = (val + 2) // 3
            heapq.heappush(max_heap, -val_new)
        
        return score
