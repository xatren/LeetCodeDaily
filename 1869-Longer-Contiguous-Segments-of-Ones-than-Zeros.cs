public class Solution {
    public bool CheckZeroOnes(string s) {
        int maxOnes = 0, maxZeros = 0;
        int currentOnes = 0, currentZeros = 0;
        
        foreach (char c in s) {
            if (c == '1') {
                currentOnes++;
                maxOnes = Math.Max(maxOnes, currentOnes);
                currentZeros = 0; 
            } else {
                currentZeros++;
                maxZeros = Math.Max(maxZeros, currentZeros);
                currentOnes = 0;
            }
        }
        
        return maxOnes > maxZeros;
    }
}
