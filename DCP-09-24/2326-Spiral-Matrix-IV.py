class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        # Create the matrix filled with -1
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        
        # Define the boundaries
        top, bottom, left, right = 0, m - 1, 0, n - 1
        
        while head:
            # Traverse top row
            for j in range(left, right + 1):
                if head:
                    matrix[top][j] = head.val
                    head = head.next
                else:
                    return matrix
            top += 1
            
            # Traverse right column
            for i in range(top, bottom + 1):
                if head:
                    matrix[i][right] = head.val
                    head = head.next
                else:
                    return matrix
            right -= 1
            
            if top <= bottom:
                # Traverse bottom row
                for j in range(right, left - 1, -1):
                    if head:
                        matrix[bottom][j] = head.val
                        head = head.next
                    else:
                        return matrix
                bottom -= 1
            
            if left <= right:
                # Traverse left column
                for i in range(bottom, top - 1, -1):
                    if head:
                        matrix[i][left] = head.val
                        head = head.next
                    else:
                        return matrix
                left += 1
        
        return matrix