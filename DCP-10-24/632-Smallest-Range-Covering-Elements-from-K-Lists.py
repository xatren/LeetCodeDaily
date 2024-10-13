import heapq

class Solution(object):
    def smallestRange(self, nums):
        \\\
        :type nums: List[List[int]]
        :rtype: List[int]
        \\\
        heap = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(heap)
        
        range_start, range_end = -float('inf'), float('inf')
        
        current_max = max(row[0] for row in nums)
        
        while len(heap) == len(nums):
            min_val, list_index, element_index = heapq.heappop(heap)
            
            if current_max - min_val < range_end - range_start:
                range_start, range_end = min_val, current_max
            
            if element_index + 1 < len(nums[list_index]):
                next_val = nums[list_index][element_index + 1]
                heapq.heappush(heap, (next_val, list_index, element_index + 1))
                current_max = max(current_max, next_val)
            else:
                break
        
        return [range_start, range_end]