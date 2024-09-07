class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(head, root):
            if not head:
                return True
           
            if not root:
                return False
            if root.val == head.val:
                return dfs(head.next, root.left) or dfs(head.next, root.right)
            return False

        if not root:
            return False
        
        if dfs(head, root):
            return True
        
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)