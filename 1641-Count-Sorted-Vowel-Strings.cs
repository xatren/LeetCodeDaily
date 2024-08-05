public class Solution {
    public int CountVowelStrings(int n) {
        int[][] dp = new int[n + 1][];
        for (int i = 0; i <= n; i++) {
            dp[i] = new int[5];
        }
        
        for (int j = 0; j < 5; j++) {
            dp[1][j] = 1;
        }
        
        for (int i = 2; i <= n; i++) {
            for (int j = 0; j < 5; j++) {
                dp[i][j] = 0;
                for (int k = j; k < 5; k++) {
                    dp[i][j] += dp[i-1][k];
                }
            }
        }
        
        int result = 0;
        for (int j = 0; j < 5; j++) {
            result += dp[n][j];
        }
        
        return result;

    }
}