# transposition cipher: encryption
# level easy

n = input() + " "
s1 = ""
s2 = ""

for i in range(len(n)):
	if n[i] == " ":
		s1 += s2[::-1]
		s1 += n[i]
		s2 = ""
	else:
		s2 += n[i]

# another method
s3 = ""
s = n.split()
for i in s:
	s3 += i[::-1]
	s3 += " "

print(s1)
print(s3)
