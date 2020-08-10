#!/bin/python3


import math
import os
import random
import re
import sys


# Calculator to parse natural language and speak in natural language
# - Only given 2 operands and all operands < 100

# sample input: 
# "add two and seven"
# "subtract six from four"

# sample output:
# "nine"
# "negative-two"

def nlp_calculator(command):
    
    numbers = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9,
        "ten" : 10,
        "eleven" : 11,
        "twelve" : 12,
        "thirteen" : 13,
        "fourteen" : 14,
        "fifteen" : 15,
        "sixteen" : 16,
        "seventeen" : 17,
        "eighteen" : 18,
        "nineteen" : 19,
        "twenty" : 20,
        "thirty" : 30,
        "forty" : 40,
        "fifty" : 50,
        "sixty" : 60,
        "seventy" : 70,
        "eighty" : 80,
        "ninety" : 90
    }

    operand_one = command.split()[1]
    if "-" in operand_one:
        temp = operand_one.split("-")
        operand_one = numbers[temp[0]] + numbers[temp[1]]
    else:
        operand_one = numbers[operand_one]
    operand_two = command.split()[3]
    if "-" in operand_two:
        temp = operand_two.split("-")
        operand_two = numbers[temp[0]] + numbers[temp[1]]
    else:
        operand_two = numbers[operand_two]
    operation = command.split()[0]

    def add(a, b):
        return a + b
    def sub(a, b):
        return b - a
    def mul(a, b):
        return a * b
    def div(a, b):
        return b // a

    operations ={
        "add" : add,
        "subtract" : sub,
        "multiply" : mul,
        "divide" : div
    }

    num = operations[operation](operand_one, operand_two)
    
    ans_string = ""

    if num < 0:
        ans_string += "negative-"
        num *= -1

    thousands = num // 1000
    hundreds = (num // 100) % 10
    tens = (num // 10) % 10
    ones = num % 10

    number = {}

    for key, val in numbers.items():
        number[val] = key

    if num in number.keys():
        return ans_string + number[num]

    if thousands != 0:
        ans_string += number[thousands] + "-thousand-"
    if hundreds != 0:
        ans_string += number[hundreds] + "-hundred-"
    if tens != 0:
        ans_string += number[tens * 10] + "-"
    if ones != 0:
        ans_string += number[ones]

    return ans_string


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    command = input()

    result = nlp_calculator(command)

    fptr.write(result + '\n')

    fptr.close()
