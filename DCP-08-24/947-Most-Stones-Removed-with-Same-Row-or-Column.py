class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        
        def dfs(node):
            stack = [node]
            while stack:
                u = stack.pop()
                for v in graph[u]:
                    if not visited[v]:
                        visited[v] = True
                        stack.append(v)
        
        graph = defaultdict(list)
        row_map = defaultdict(list)
        col_map = defaultdict(list)
        
        for i, (x, y) in enumerate(stones):
            row_map[x].append(i)
            col_map[y].append(i)
        
        for indices in row_map.values():
            for i in range(len(indices) - 1):
                for j in range(i + 1, len(indices)):
                    graph[indices[i]].append(indices[j])
                    graph[indices[j]].append(indices[i])
        
        for indices in col_map.values():
            for i in range(len(indices) - 1):
                for j in range(i + 1, len(indices)):
                    graph[indices[i]].append(indices[j])
                    graph[indices[j]].append(indices[i])
        
        visited = [False] * len(stones)
        max_removed = 0
        
        for i in range(len(stones)):
            if not visited[i]:
                visited[i] = True
                component_size = 0
                stack = [i]
                while stack:
                    node = stack.pop()
                    component_size += 1
                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)
                max_removed += (component_size - 1)
        
        return max_removed
