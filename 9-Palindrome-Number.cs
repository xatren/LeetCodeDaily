public class Solution {
    public bool IsPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        string original = x.ToString();
        char[] charArray = original.ToCharArray();
        Array.Reverse(charArray);
        string reversed = new string(charArray);

        return original == reversed;
    }
}
