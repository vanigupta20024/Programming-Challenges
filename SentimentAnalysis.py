# GHC Codepath - Sandbox 8

#!/bin/python3

import math
import os
import random
import re
import sys

# Given:
# - list of words
# - list of scores
# - list of sentences
# for each sentence in list of sentences, output
# an integer in a list of integers that indicates what
# total sentiment score the sentences have

# sample input
# words = ["amazing", "sad", "great", "no", "yes", "angry", "happy"]
# scores = [0.4, -0.8, -0.1, 0.1. -0.7, 0.8]
# sentences = [
# "that makes me so happy! amazing.",
# "I'm so angry about this sad thing.",
# "sad but true, amazing",
# "yes that is great, and amazing"
# ]
# sample output:
# [1.2000000000000002, -1.5, -0.4, 1.3]


def sentimentAnalyzer(words, scores, text):
    
    word_scores = {}
    for index in range(len(words)):
        word_scores[words[index]] = scores[index]
    
    int_list = []
    for sentence in text:
        sentiment_score = 0
        for word in sentence.split():
            word = word.replace('!',"").replace('?',"").replace(',',"").replace('.',"")
            if word in word_scores.keys():
                sentiment_score += word_scores[word]
        int_list.append(sentiment_score)

    return int_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    words_count = int(input().strip())

    words = []

    for _ in range(words_count):
        words_item = input()
        words.append(words_item)

    scores_count = int(input().strip())

    scores = []

    for _ in range(scores_count):
        scores_item = float(input().strip())
        scores.append(scores_item)

    text_count = int(input().strip())

    text = []

    for _ in range(text_count):
        text_item = input()
        text.append(text_item)

    result = sentimentAnalyzer(words, scores, text)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
