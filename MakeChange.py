# GHC Codepath SE101 
# Sandbox - 11 - basic

#!/bin/python3
# Complete the 'coinChange' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER amount
#  2. INTEGER_ARRAY coins
# This function will determine the fewest coins
# are needed to reach the total in amount given
# the denominations in coins. 

'''
Sample input: Amount = 11, coins = [1,2,5]
Sample output: 3 (as 5+5+1)

Sample input: Amount = 3, coins = [2]
Sample output: -1
'''

def coinChange(amount, coins):
    coins = sorted(coins, reverse = True)
    count = 0
    i = 0
    while amount > 0 and amount >= coins[-1]:
        if amount >= coins[i]:
            count += 1
            amount -= coins[i]
        else:
            i += 1
    if count == 0 or amount != 0:
        return -1
    return count
if __name__ == '__main__':
