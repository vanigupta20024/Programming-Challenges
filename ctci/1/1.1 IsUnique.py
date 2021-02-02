# To determine if all the characters in string are unique or not.

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
