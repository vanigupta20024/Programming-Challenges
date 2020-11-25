'''
Suppose you have a long flowerbed in which some of the plots are planted and some are not. 
However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), 
and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
'''

class Solution:
    def canPlaceFlowers(self, fbed: List[int], n: int) -> bool:
        free_spots = 0
        for i in range(len(fbed)):
            if fbed[i] == 0 and (i == 0 or fbed[i-1] == 0) and (i == len(fbed) - 1 or fbed[i+1] == 0):
                fbed[i] = 1
                free_spots += 1
            if free_spots >= n:
                return True
        return False
