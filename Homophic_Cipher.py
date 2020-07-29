key_table = {'A':'D9', 'B':'X', 'C':'S', 'D':'F', 'E':'Z721', 'F':'E', 'G':'H', 'H':'C', 'I':'V3',
            'J':'I', 'K':'T', 'L':'P', 'M':'G', 'N':'A5', 'O':'Q0', 'P':'L', 'Q':'K', 'R':'J',
            'S':'R4', 'T':'6U', 'U':'O', 'V':'W', 'W':'M', 'X':'Y', 'Y':'B', 'Z':'N'}

import random
s = input()
def encrypt(s):
    st = ""
    for item in s:
        if item.upper() in key_table:
            st += random.choice(key_table[item.upper()])
        else:
            st += item
    return st

def getkey(val):
    for k, v in key_table.items():
        if val in v:
            return k

def decrypt(s):
    words = s.split()
    res = ""
    for word in words:
        for letter in word:
            res += getkey(letter)
        res += " "
    return res

print("Encryption of message:{} => {}".format(s, encrypt(s)))
print("Decryption of message:{} => {}".format(encrypt(s), decrypt(encrypt(s))))
