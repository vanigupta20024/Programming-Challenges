'''
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.

It's guaranteed that a unique mapping will always exist.

Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
'''

class Solution:
    def freqAlphabets(self, s: str) -> str:
        arr = []
        s = s[::-1]
        i = 0
        while i + 2 < len(s):
            if s[i] == "#":
                arr.append(str(int(s[i+2] + s[i+1])))
                i += 3
            else:
                arr.append(s[i])
                i += 1
        ans = ""
        while i < len(s):
            arr.append(s[i])
            i += 1
        for i in arr:
            ans += chr(ord('a') + int(i) - 1)
        return ans[::-1]
            
