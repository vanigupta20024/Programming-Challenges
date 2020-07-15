# Intermediate version of stock ticker:
# Given an array of stock ticker strings, where one string represents a day of trading, 
# Write a function that finds the greatest window of return between two stocks
# and return the stock, the buy index, and the sell index
# "AAPL 114 GOOG 545 TSLA 33"
# "AAPL 113 GOOG 533 TSLA 23"
# "AAPL 112 GOOG 556 TSLA 34"
# "1 2 TSLA" - buy TSLA on day 1 and sell on day 2 for a 47% increase 


print("Enter stocks and their values day-wise: ")

lines = []
while True:
	line = input()
	if line:
		lines.append(line)
	else:
		break

stock = {}
for line in lines:
	s = line.split()
	for index in range(0, len(s), 2):
		if s[index] not in stock.keys():
			stock[s[index]] = [int(s[index + 1])]
		else:
			stock[s[index]].append(int(s[index + 1]))
print(stock)

def calc_perc(num_one, num_two):
	return ((num_one - num_two)/num_two) * 100

max_stock = ""
max_window = day_one = day_two = 0
for key, val in stock.items():
	for i in range(len(val)):
		for j in range(i+1, len(val)):
			if calc_perc(val[j], val[i]) > max_window:
				max_window = calc_perc(val[j], val[i])
				max_stock = key
				day_one = i + 1
				day_two = j + 1

print("Max Stock: {}, Max Percentage increase: {}, Day 1: {}, Day 2: {}.".format(max_stock, round(max_window,3), day_one, day_two))
	
