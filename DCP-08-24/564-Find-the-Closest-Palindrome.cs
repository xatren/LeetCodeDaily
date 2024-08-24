public class Solution {
    public string NearestPalindromic(string n) {
        if (n == "1") return "0";

        int len = n.Length;
        long num = long.Parse(n);
        
        HashSet<long> candidates = new HashSet<long>();
        
        candidates.Add((long)Math.Pow(10, len) + 1);      
        candidates.Add((long)Math.Pow(10, len - 1) - 1); 
        
        long firstHalf = long.Parse(n.Substring(0, (len + 1) / 2));
        
        foreach (long i in new long[] {firstHalf - 1, firstHalf, firstHalf + 1}) {
            string prefix = i.ToString();
            string candidate;
            if (len % 2 == 0) {
                candidate = prefix + ReverseString(prefix);
            } else {
                candidate = prefix + ReverseString(prefix.Substring(0, prefix.Length - 1));
            }
            candidates.Add(long.Parse(candidate));
        }
        
        candidates.Remove(num);
        
        long closest = -1;
        foreach (long candidate in candidates) {
            if (closest == -1 || 
                Math.Abs(candidate - num) < Math.Abs(closest - num) || 
                (Math.Abs(candidate - num) == Math.Abs(closest - num) && candidate < closest)) {
                closest = candidate;
            }
        }
        
        return closest.ToString();
    }
    
    private string ReverseString(string s) {
        char[] array = s.ToCharArray();
        Array.Reverse(array);
        return new string(array);
    }
}
