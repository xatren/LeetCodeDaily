# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthLargestLevelSum(self, root, k):
        if not root:
            return -1
    
        level_sums = []
        queue = [root]

        while queue:
            level_size = len(queue)
            level_sum = 0
        
            for _ in range(level_size):
                node = queue.pop(0)
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level_sums.append(level_sum)
    
        if len(level_sums) < k:
            return -1

        level_sums.sort(reverse=True)
        return level_sums[k-1]
        