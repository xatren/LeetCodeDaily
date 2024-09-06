class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num_set = set(nums)
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        current = head
        
        while current:
            if current.val in num_set:
                prev.next = current.next
            else:
                prev = current
            
            current = current.next
        
        return dummy.next