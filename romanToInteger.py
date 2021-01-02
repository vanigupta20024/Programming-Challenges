'''
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        } 
        number = roman[s[0]]
        for i in range(1, len(s)):
            if ((s[i]=="V" or s[i]=="X") and s[i-1]=="I") or ((s[i]=="L" or s[i]=="C") and s[i-1]=="X") or ((s[i]=="D" or s[i]=="M") and s[i-1]=="C"):
                number = number - 2*roman[s[i-1]]
            number += roman[s[i]]
        return number
