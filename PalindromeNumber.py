class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        if x % 10 == 0 and x != 0: 
            return False
        
        # x = str(x)
        # if x == x[::-1]:
        #     return True
        # return False
        
        rev_num = 0
        while x > rev_num:
            rev_num = rev_num * 10 + x % 10
            x //= 10
            
        if x == rev_num or x == rev_num // 10:
            return True
        return False
