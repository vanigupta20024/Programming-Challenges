'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.
'''

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = a = l = o = n = 0
        for i in text:
            if i == 'b': b += 1
            elif i == 'a': a += 1
            elif i == 'l': l += 1
            elif i == 'n': n += 1
            elif i == 'o': o += 1
        count = 0
        while b and a and l and o and n:
            if b and a and l - 1 and o - 1 and n:
                count += 1
                b =- 1
                a -= 1
                l -= 2
                o -= 2
                n -= 1
            else: break
        return count
