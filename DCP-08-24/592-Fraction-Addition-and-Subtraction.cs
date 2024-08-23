using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

public class Solution {
    public string FractionAddition(string expression) {
        var matches = Regex.Matches(expression, @\[+-]?\\d+/\\d+\);
        
        int numerator = 0;
        int denominator = 1;
        
        foreach (Match match in matches) {
            string frac = match.Value;
            string[] parts = frac.Split('/');
            int num = int.Parse(parts[0]);
            int denom = int.Parse(parts[1]);
            
            numerator = numerator * denom + num * denominator;
            denominator *= denom;
            
            int gcd = GCD(Math.Abs(numerator), denominator);
            numerator /= gcd;
            denominator /= gcd;
        }
        
        return $\{numerator}/{denominator}\;
    }
    
    private int GCD(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}
