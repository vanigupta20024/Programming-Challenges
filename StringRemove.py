'''
Remove the unwanted string from the particular 1st string and display the remaining alphabets in 
alphabetical order with each remaining alphabet followed by number of times it appears.
Input:
abcdefghijk abcd

Output:
e1f1g1h1i1j1k1
'''

n1, n2 = input().split()

frequence = [0 for _ in range(26)]
for i in range(len(n1)):
    frequence[ord(n1[i]) - ord('a')] += 1
    
for i in range(len(n2)):
    frequence[ord(n2[i]) - ord('a')] = 0

for i in range(26):
    if frequence[i] != 0:
        print(chr(i+ord('a'))+str(int(frequence[i])), end = "")
