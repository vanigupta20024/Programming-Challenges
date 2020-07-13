'''
Encrypting and decrypting using XOR

test-samples:
input: 
	vani
	a
output:
Encoded string is:  ↨ ☼
Decoded string is: vani

'''

print("Enter string to be encoded: ", end = "")
s = input()
print("Enter alphabet as a key: ", end = "")
k = input()
st = ""

for i in range(len(s)):
	# using XOR to encrypt string
	st += chr(ord(s[i])^ord(k))
print("Encoded string is: ",st)

# decrypting and printing string
# any number or alphabet when XORed twice
# gives same value as input
print("Decoded string is: ", end = "")
for i in range(len(s)):
	print(chr(ord(st[i])^ord(k)), end = "")
