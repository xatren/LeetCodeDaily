import heapq

class Solution(object):
    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        times = sorted((arrival, leaving, i) for i, (arrival, leaving) in enumerate(times))
        
        available_chairs = list(range(len(times)))  
        occupied_chairs = []  
        
        for arrival, leaving, friend in times:
            while occupied_chairs and occupied_chairs[0][0] <= arrival:
                _, chair = heapq.heappop(occupied_chairs)
                heapq.heappush(available_chairs, chair)
            
            chair = heapq.heappop(available_chairs)
            
            if friend == targetFriend:
                return chair
            
            heapq.heappush(occupied_chairs, (leaving, chair))
        
        return -1