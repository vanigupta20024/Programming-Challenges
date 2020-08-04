string = input("Enter text: ")
key = input("Enter alphabetical key/primer: ")
if len(key) < len(string):
    key = (key + string)[: len(string)]
elif len(key) > len(string):
    key = key[: len(string)]

def encrypt():
    enc = ""
    s = 0
    v = ''
    for i in range(len(string)):
        if string[i].isalpha():
            if string[i].isupper():
                v = 'A'
            else:
                v = 'a'
            s = (ord(string[i]) - ord(v) + ord(key[i]) - ord(v)) % 26
            enc += chr(s + ord(v))
        else:
            enc += string[i]
    return enc

def decrypt(string):
    dec = ""
    s = 0
    v = ''
    for i in range(len(string)):
        if string[i].isalpha():
            if string[i].isupper():
                v = 'A'
            else:
                v = 'a'
            s = ord(string[i]) - ord(key[i])
            if s < 0:
                s += 26
            dec += chr(s + ord(v))
        else:
            dec += string[i]
    return dec

print("Encrypted text:", encrypt())
print("Decrypted text:", decrypt(encrypt()))
