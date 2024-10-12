import heapq

class Solution(object):
    def minGroups(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[0])
        
        heap = []
        
        for start, end in intervals:
            if heap and start > heap[0]:
            
                heapq.heapreplace(heap, end)
            else:
                heapq.heappush(heap, end)
        
        return len(heap)