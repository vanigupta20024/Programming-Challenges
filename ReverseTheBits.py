# CodePath-SE101
# Statement: 
# Given an integer greater than 9, print all the bits in the reverse order, 1's value first, 
# and then 2's value and then the 4's value, and then the 8's value and so on, with a space in between.


# take user input
a = int(input())
b = ""

# converting user input into binary
while a > 0:
  b += str(a%2)
  a = a//2

# as we have already made a string 
# in reverse order, there's no need to reverse it again
# converting binary string to int list
l1 = [int(i) for i in b]

power = 1

# reverse looping through binary string
for i in reversed(range(len(b))):
  l1[i] *= power
  power *= 2
  
# final answer
print(sum(l1))
