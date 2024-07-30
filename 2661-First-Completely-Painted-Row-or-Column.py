class Solution(object):
    def firstCompleteIndex(self, arr, mat):    
        num_to_pos = {}
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                num_to_pos[mat[r][c]] = (r, c)
        
        row_count = [0] * len(mat)
        col_count = [0] * len(mat[0])
        
        painted = set()
        
        for i, num in enumerate(arr):
            if num in painted:
                continue
            painted.add(num)
            
            r, c = num_to_pos[num]
            
            row_count[r] += 1
            col_count[c] += 1
            
            if row_count[r] == len(mat[0]) or col_count[c] == len(mat):
                return i
        
        return -1
