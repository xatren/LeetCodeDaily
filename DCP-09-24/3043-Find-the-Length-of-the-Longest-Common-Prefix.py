class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        # Convert all integers to strings
        arr1 = [str(x) for x in arr1]
        arr2 = [str(x) for x in arr2]
        
        # Create a set of all prefixes for arr1
        prefixes1 = set()
        for num in arr1:
            for i in range(1, len(num) + 1):
                prefixes1.add(num[:i])
        
        # Find the longest common prefix
        max_length = 0
        for num in arr2:
            for i in range(1, len(num) + 1):
                prefix = num[:i]
                if prefix in prefixes1:
                    max_length = max(max_length, len(prefix))
                else:
                    break  # No need to check longer prefixes
        
        return max_length