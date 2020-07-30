# Vignere cipher
# Case of Input and key should be same

inp = input("Enter string: ")
key = input("Enter key: ")

if len(key) > len(inp):
    print("Enter a key string with lesser characters!")
    exit()

elif len(key) < len(inp):
    key = (key * ((len(inp) // len(key)) + 1))[:len(inp)]

def v_encrypt(inp, key):
    res = ""
    for i in range(len(inp)):
        if inp[i].isupper(): v = 'A'
        else: v = 'a'
        res += (chr(((ord(inp[i]) - 2 * ord(v) + ord(key[i])) % 26) + ord(v)))
    return res

def v_decrypt(enc, key):
    res = ""
    for i in range(len(enc)):
        if inp[i].isupper(): v = 'A'
        else: v = 'a'
        s = ord(enc[i]) - ord(key[i])
        if s < 0: s += 26
        res += chr(s + ord(v))

    return res

e = v_encrypt(inp, key)
d = v_decrypt(e, key)
print("Encoded: {} and Decoded: {}".format(e, d))
