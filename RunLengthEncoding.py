'''
Given a string, Your task is to  complete the function encode that returns the run length encoded string for the given string.
eg if the input string is “wwwwaaadexxxxxx”, then the function should return “w4a3d1e1x6″.
You are required to complete the function encode that takes only one argument the string which is to be encoded and returns the encoded string.
'''

def encode(s):
    if len(s) == 1:
        return s + "1"
    i = 1
    count = 1
    st = s[0]
    while i < len(s):
        if s[i - 1] == s[i]:
            i += 1
            count += 1
        else:
            st += str(count) + s[i]
            count = 1
            i += 1
        if i == len(s):
            st += str(count)
            i += 1
    return st
