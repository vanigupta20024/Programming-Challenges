# GHC Codepath SE101
# Basic to intermediate

# task pascal's triangle

# [1]
# [1,1]
# [1,2,1]
# [1,3,3,1]
# [1,4,6,4,1] ....

# pattern => starts and ends with 1
# middle element in middle row are one less than elements 
# previous row

print("Enter integer input for pascal's triangle: ", end = "")
n = int(input())

triangle = []
current_row = [1]
triangle.append(current_row)

for i in range(n-1):
	row = []
	row.append(1)
	for j in range(1, len(current_row)):
		row.append(current_row[j-1] + current_row[j])
	row.append(1)
	current_row = row
	triangle.append(row)

for i in triangle:
	print(i)
