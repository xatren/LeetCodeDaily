class Solution(object):
    def numberOfPowerfulInt(self, start, finish, limit, s):
        """
        :type start: int
        :type finish: int
        :type limit: int
        :type s: str
        :rtype: int
        """
        s_start = str(start)
        s_finish = str(finish)
        suffix = s

        if len(suffix) > len(s_finish):
            return 0
        
        def count_powerful_up_to(upper):
            if int(upper) < int(suffix):
                return 0
                
            n = len(upper)
            m = len(suffix)
            
            # If suffix is the same length as upper, we just need to check if upper >= suffix
            # and if all digits in upper are within limit
            if n == m:
                if int(upper) >= int(suffix) and all(int(digit) <= limit for digit in upper):
                    return 1
                return 0
            
            if not all(int(digit) <= limit for digit in suffix):
                return 0
            
            # dp[i][tight] represents number of valid prefixes for first i positions
            # tight indicates whether we're bounded by upper bound
            dp = {}
            
            def solve(pos, tight, started):
                if pos == n:
                    return 1
                
                if (pos, tight, started) in dp:
                    return dp[(pos, tight, started)]
                
                result = 0
                
                # Current position is in the suffix part
                if pos >= n - m:
                    suffix_digit = int(suffix[pos - (n - m)])
                    if not tight or int(upper[pos]) >= suffix_digit:
                        # Check if current digit in suffix is within limit
                        if suffix_digit <= limit:
                            result = solve(pos + 1, tight and int(upper[pos]) == suffix_digit, True)
                else:
                    # Current position is not in the suffix part
                    max_digit = int(upper[pos]) if tight else limit
                    
                    if not started:
                        result = solve(pos + 1, False, False)
                        
                        for d in range(1, max_digit + 1):
                            if d <= limit:
                                result += solve(pos + 1, tight and d == int(upper[pos]), True)
                    else:
                        for d in range(max_digit + 1):
                            if d <= limit:
                                result += solve(pos + 1, tight and d == int(upper[pos]), True)
                
                dp[(pos, tight, started)] = result
                return result
            
            return solve(0, True, False)
        
        count_up_to_finish = count_powerful_up_to(s_finish)
        count_up_to_start_minus_one = count_powerful_up_to(str(start - 1))
        
        return count_up_to_finish - count_up_to_start_minus_one