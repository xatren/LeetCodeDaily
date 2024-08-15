class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        five_dollar_bills = 0
        ten_dollar_bills = 0
        
        for bill in bills:
            if bill == 5:
                five_dollar_bills += 1
            elif bill == 10:
                if five_dollar_bills == 0:
                    return False
                five_dollar_bills -= 1
                ten_dollar_bills += 1
            elif bill == 20:
                if ten_dollar_bills > 0 and five_dollar_bills > 0:
                    ten_dollar_bills -= 1
                    five_dollar_bills -= 1
                elif five_dollar_bills >= 3:
                    five_dollar_bills -= 3
                else:
                    return False
        
        return True