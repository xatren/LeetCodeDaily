# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        # Count the length of the linked list
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        
        # Calculate the base size and extra nodes
        base_size, extra = divmod(length, k)
        
        # Create the result array
        result = [None] * k
        curr = head
        for i in range(k):
            if not curr:
                break
            
            result[i] = curr
            
            # Calculate the size of the current part
            part_size = base_size + (1 if extra > 0 else 0)
            
            # Traverse to the end of the current part
            for _ in range(part_size - 1):
                curr = curr.next
            
            # Cut off the link to the next part
            next_node = curr.next
            curr.next = None
            curr = next_node
            
            extra -= 1
        
        return result