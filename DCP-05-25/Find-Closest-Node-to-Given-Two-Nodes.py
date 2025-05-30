class Solution(object):
    def closestMeetingNode(self, edges, node1, node2):
        """
        :type edges: List[int]
        :type node1: int
        :type node2: int
        :rtype: int
        """
        n = len(edges)
        
        def getDist(start):
            """Get distances from start node to all reachable nodes"""
            dist = [-1] * n  
            dist[start] = 0
            curr = start
            
            while curr != -1 and edges[curr] != -1:
                next_node = edges[curr]
                if dist[next_node] != -1:
                    break
                dist[next_node] = dist[curr] + 1
                curr = next_node
                
            return dist
        
        dist1 = getDist(node1)
        dist2 = getDist(node2)
        
        min_max_dist = float('inf')
        result = -1
        
        for i in range(n):
            if dist1[i] != -1 and dist2[i] != -1:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_max_dist:
                    min_max_dist = max_dist
                    result = i
                elif max_dist == min_max_dist and i < result:
                    result = i
        
        return result