class Solution(object):
    def diffWaysToCompute(self, expression):
        \\\
        :type expression: str
        :rtype: List[int]
        \\\
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    if op == '+':
                        results.append(l + r)
                    elif op == '-':
                        results.append(l - r)
                    elif op == '*':
                        results.append(l * r)
            return results
        
        def dfs(s):
            if s in memo:
                return memo[s]
            
            if s.isdigit():
                return [int(s)]
            
            results = []
            for i, char in enumerate(s):
                if char in ['+', '-', '*']:
                    left = dfs(s[:i])
                    right = dfs(s[i+1:])
                    results.extend(compute(left, right, char))
            
            memo[s] = results
            return results
        
        memo = {}
        return dfs(expression)