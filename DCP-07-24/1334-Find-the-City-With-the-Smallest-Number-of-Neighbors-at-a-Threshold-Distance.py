class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        dist = [[float('inf')] * n for _ in range(n)]
        
        # Distance from a city to itself is 0
        for i in range(n):
            dist[i][i] = 0
        
        # Populate the distance matrix with given edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Floyd-Warshall algorithm to find shortest paths
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Find the city with the smallest number of reachable cities
        # within the distance threshold
        min_reachable_count = float('inf')
        result_city = -1
        
        for i in range(n):
            reachable_count = 0
            for j in range(n):
                if i != j and dist[i][j] <= distanceThreshold:
                    reachable_count += 1
            
            if reachable_count < min_reachable_count or (reachable_count == min_reachable_count and i > result_city):
                min_reachable_count = reachable_count
                result_city = i
        
        return result_city