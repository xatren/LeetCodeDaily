class Solution(object):
    def findMinDifference(self, timePoints):
        \\\
        :type timePoints: List[str]
        :rtype: int
        \\\
        # Convert time to minutes
        def convert_to_minutes(time):
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes
        
        # Convert all times to minutes
        minutes = sorted(convert_to_minutes(time) for time in timePoints)
        
        # Calculate differences
        n = len(minutes)
        min_diff = float('inf')
        
        # Check differences between adjacent times
        for i in range(1, n):
            diff = minutes[i] - minutes[i-1]
            min_diff = min(min_diff, diff)
        
        # Check wrap-around case (between last and first time)
        wrap_diff = (minutes[0] + 1440) - minutes[-1]
        min_diff = min(min_diff, wrap_diff)
        
        return min_diff