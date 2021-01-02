'''
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.
Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # if len(digits) > 0: 
        #     num = int("".join([str(i) for i in digits])) + 1
        #     num = [int(i) for i in str(num)]
        # if len(num) < len(digits):
        #     num = [0] * (len(digits) - len(num)) + num
        # return num
        
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            if digits[i] != 10:
                return digits
            digits[i] = 0
        
        return [1] + digits
