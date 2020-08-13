def encrypt():
	txt = input("Enter string: ")
	key = input("Enter key: ")
	key = key.lower()

	s = ""
	for i in key:
		if i not in s: s+= i

	key = s
	l = [i for i in key]
	key2 = sorted(list(l))

	if len(key) > len(txt):
	    key = key[:len(txt)]

	cols = len(key2)
	rows = -(-len(txt)//cols)
	enc_text = ""

	matrix = [[None for c in range(cols)] for r in range(rows)]

	index = 0
	for r in range(rows):
		for c in range(cols):
			if index < len(txt):
				matrix[r][c] = txt[index]
				index += 1
	for i in matrix: print(i)

	for i in key2:
		x = key.index(i)
		enc_text += "".join([row[x] for row in matrix if row[x] is not None])
	return enc_text

def decrypt():
	txt = input("Enter string: ")
	key = input("Enter key: ")
	key = key.lower()

	s = ""
	for i in key:
		if i not in s: s+= i

	key = s
	l = [i for i in key]
	key2 = sorted(list(l))

	if len(key) > len(txt):
	    key = key[:len(txt)]

	cols = len(key2)
	rows = -(-len(txt)//cols)
	dec_text = ""
	end = len(txt) % len(key2)

	matrix = [[" " for c in range(cols)] for r in range(rows)]
	diff = len(key) - (len(txt) % len(key))
	if diff == len(key):
		diff = 0

	cl = -1
	while diff != 0:
		matrix[-1][cl] = None
		diff -= 1
		cl -= 1

	indx = 0
	for i in key2:
		x = key.index(i)
		for r in range(rows):
			if matrix[r][x] is not None and indx < len(txt):
				matrix[r][x] = txt[indx]
				indx += 1
	for i in matrix:
		print(i)

	for r in range(rows):
		for c in range(cols):
			if matrix[r][c] is not None:
				dec_text += matrix[r][c]
	print(dec_text)

print(encrypt())
decrypt()
