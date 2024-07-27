class Solution:
    def minimumCost(self, source, target, original, changed, cost):
        # Initialize the max possible cost
        inf = float('inf')
        n = len(source)
        
        # Map for the transformation costs
        min_cost = [[inf] * 26 for _ in range(26)]
        
        # Set the cost for no change (x to x) to 0
        for i in range(26):
            min_cost[i][i] = 0
        
        # Update the min_cost with given transformations
        for i in range(len(original)):
            src = ord(original[i]) - ord('a')
            dest = ord(changed[i]) - ord('a')
            min_cost[src][dest] = min(min_cost[src][dest], cost[i])
        
        # Floyd-Warshall algorithm to find minimum transformation cost for each pair
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    min_cost[i][j] = min(min_cost[i][j], min_cost[i][k] + min_cost[k][j])
        
        # Calculate the total cost to transform source to target
        total_cost = 0
        for i in range(n):
            src = ord(source[i]) - ord('a')
            tgt = ord(target[i]) - ord('a')
            if src == tgt:
                continue
            if min_cost[src][tgt] == inf:
                return -1
            total_cost += min_cost[src][tgt]
        
        return total_cost
