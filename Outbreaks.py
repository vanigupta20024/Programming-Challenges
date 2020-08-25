# GHC Codepath - Sandbox 8
# Module SE101

#!/bin/python3

import math
import os
import random
import re
import sys
import json

# Given a segment of a map with map coordinates as keys
# and count of outbreaks in the area as values
# - Find the center of the outbreak
# - treat each case as 1 data-point

# sample input:
# reported_outbreak = {
# "5,5": 10,
# "5,6": 8,
# "5,4": 8,
# "4,5": 8,
# "4,6": 8,
# "6,6": 7,
# "6,5": 8,
# "4,4": 8,
# "3,4": 4,
# "3,3": 2,
# "6,7": 2
# }

# sample output:
# The center is: "5,5"

def findCenter(points):
    outbreak = json.loads(points)

    sum_x = 0
    sum_y = 0

    sum_outbreak = 0

    for key, value in outbreak.items():
        x,y = map(int, key.split(','))
        sum_x += x * value
        sum_y += y * value
        sum_outbreak += value

    x_coordinate = str(round(sum_x/sum_outbreak))
    y_coordinate = str(round(sum_y/sum_outbreak))
    
    answer = ','.join([x_coordinate, y_coordinate])
    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    points = input()

    result = findCenter(points)

    fptr.write(result + '\n')

    fptr.close()
