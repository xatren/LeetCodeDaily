class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        n = len(skill)
        skill.sort()  # Sort the array
        
        # required skill for each team
        total_skill = sum(skill)
        if total_skill % (n // 2) != 0:
            return -1
        
        required_skill = total_skill // (n // 2)
        
        left, right = 0, n - 1
        chemistry_sum = 0
        
        while left < right:
            if skill[left] + skill[right] != required_skill:
                return -1
            
            chemistry_sum += skill[left] * skill[right]
            left += 1
            right -= 1
        
        return chemistry_sum