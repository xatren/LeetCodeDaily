# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def gcd(self, a, b):
        """Calculate the Greatest Common Divisor of a and b."""
        while b:
            a, b = b, a % b
        return a

    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        current = head
        while current.next:
            gcd_value = self.gcd(current.val, current.next.val)
            new_node = ListNode(gcd_value)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next

        return head