class Solution(object):
    def minOperations(self, boxes):
        n = len(boxes)
        answer = [0] * n

        # Convert string
        nums = [int(b) for b in boxes]

        for i in range(n):
            moves = 0
            for j in range(n):
                if i != j and nums[j] == 1:
                    moves += abs(j - i)
            answer[i] = moves
                
        return answer
        