'''
Caesar cipher:
Encryption technique also called the shift cipher.
Each letter is shifted with respect to a key value entered.
'''
print("Enter 0 for encryption and 1 for decryption:")
n = int(input())
enc_text = ""
print("Enter the input string: ", end = "")
text = input()
print("Enter key: ", end = "")
key = int(input())


if n == 0:
	
	# encryption process
	for index in range(len(text)):

	 	# checking if element is an alphabet
		if text[index].isalpha():
			if text[index].isupper():
				temp = (ord(text[index]) - ord('A') + key) % 26 + ord('A')
				enc_text += chr(temp)

			elif text[index].islower():
				temp = (ord(text[index]) - ord('a') + key) % 26 + ord('a')
				enc_text += chr(temp)
		else:
	 		# if not alphabet, simply append without changes
			enc_text += text[index]

	print("Old text: {0}\nEncrypted text: {1}".format(text, enc_text))

if n == 1:

	# decryption process
	for index in range(len(text)):

		# checking if element is an alphabet
		if text[index].isalpha():
			if text[index].isupper():
				temp = (ord(text[index]) - ord('A') - key)
				if temp < 0:
					temp += 26
				temp += ord('A')
				enc_text += chr(temp)

			elif text[index].islower():
				temp = (ord(text[index]) - ord('a') - key)
				if temp < 0:
					temp += 26
				temp += ord('a')
				enc_text += chr(temp)
		else:
			# if not alphabet, simply append without changes
			enc_text += text[index]

	print("Old text: {0}\nDecrypted text: {1}".format(text, enc_text))
