# To determine if all the characters in string are unique or not.

# Method 1:
def isUnique(s):
    if len(s) < 1:
        return 0
    dic = {}
    for i in s:
        if i in dic:
            return 0
        else:
            dic[i] = 1
    return 1
    
s = input()
print(isUnique(s))

# Method 2:
def isUnique(s):
    checker = 0
    for i in range(len(s)):
        val = ord(s[i]) - ord('a')
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val)
    return True

s = input()
print(isUnique(s))
