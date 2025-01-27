class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # Create adjacency matrix to represent prerequisites
        dp = [[False] * numCourses for _ in range(numCourses)]
        
        # Fill prerequisites
        for pre, course in prerequisites:
            dp[pre][course] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    dp[i][j] = dp[i][j] or (dp[i][k] and dp[k][j])
        
        # Answer each query
        return [dp[u][v] for u, v in queries]