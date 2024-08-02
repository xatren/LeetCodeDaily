public class Solution {
    public int MinSwaps(int[] nums) {
        int n = nums.Length;
        int totalOnes = nums.Count(num => num == 1);

        if (totalOnes == 0 || totalOnes == n) {
            return 0;
        }

        int[] extendedNums = new int[2 * n];
        for (int i = 0; i < n; i++) {
            extendedNums[i] = nums[i];
            extendedNums[i + n] = nums[i];
        }

        int currentOnes = 0;
        for (int i = 0; i < totalOnes; i++) {
            if (extendedNums[i] == 1) {
                currentOnes++;
            }
        }

        int minSwaps = totalOnes - currentOnes;

        for (int i = 1; i < n; i++) {
            if (extendedNums[i - 1] == 1) {
                currentOnes--;
            }
            if (extendedNums[i + totalOnes - 1] == 1) {
                currentOnes++;
            }
            minSwaps = Math.Min(minSwaps, totalOnes - currentOnes);
        }

        return minSwaps;
    }
}
