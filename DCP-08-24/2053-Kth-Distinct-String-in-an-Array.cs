public class Solution {
    public string KthDistinct(string[] arr, int k) {
        Dictionary<string, int> frequency = new Dictionary<string, int>();
        foreach (var str in arr) {
            if (frequency.ContainsKey(str)) {
                frequency[str]++;
            } else {
                frequency[str] = 1;
            }
        }
        
        List<string> distinctStrings = new List<string>();
        foreach (var str in arr) {
            if (frequency[str] == 1) {
                distinctStrings.Add(str);
            }
        }
        
        
        if (distinctStrings.Count >= k) {
            return distinctStrings[k - 1];
        } else {
            return "";
        }

    }
}