enc_key = {
		'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V', 'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R',
		'J' : 'Q', 'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L', 'P' : 'K', 'Q' : 'J', 'R' : 'I', 
		'S' : 'H', 'T' : 'G', 'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A', 'a' : 'z', 
		'b' : 'y', 'c' : 'x', 'd' : 'w', 'e' : 'v', 'f' : 'u', 'g' : 't', 'h' : 's', 'i' : 'r', 'j' : 'q', 
		'k' : 'p', 'l' : 'o', 'm' : 'n', 'n' : 'm', 'o' : 'l', 'p' : 'k', 'q' : 'j', 'r' : 'i', 's' : 'h', 
		't' : 'g', 'u' : 'f', 'v' : 'e', 'w' : 'd', 'x' : 'c', 'y' : 'b', 'z' : 'a'}

string = input("Enter: ")

def encrypt(string):
	
	enc_text = ""
	for i in range(len(string)):
		if string[i] in enc_key:
			enc_text += enc_key[string[i]]
		else:
			enc_text += string[i]
	return enc_text

print("Encrypted:", encrypt(string))
print('Decrypted:', encrypt(encrypt(string)))
