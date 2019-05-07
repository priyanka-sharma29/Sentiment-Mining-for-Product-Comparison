#!/usr/bin/env python
from __future__ import division
# Importing all necessary modules
import os
import re
import sys
import time
import json
import string

# Defining our sentiments dictionary
sentiment_Dictionary = {'positive': {}, 'negative': {}}

# Defining function to load the positive and negative bag of words
def load_Sentiments():
    with open('/home/cloudera/Downloads/FinalProject/Sentiments/positive-words.txt', 'r') as posFile:
        for line in posFile:
            sentiment_Dictionary['positive'][line.strip()] = 1

    with open('/home/cloudera/Downloads/FinalProject/Sentiments/negative-words.txt', 'r') as negFile:
        for line in negFile:
            sentiment_Dictionary['negative'][line.strip()] = 1

# Defining the mapper function
def main():
    load_Sentiments()

    for twt_Obj in sys.stdin:

        twt_Obj = twt_Obj.strip().split('\t')
        userId = twt_Obj[0].strip()

        twt_Txt = twt_Obj[1].lower()
        twt_Txt = re.sub('[^a-zA-Z]', ' ', twt_Txt)

        words = {}
        for w in twt_Txt.split():
            if len(w) > 0:
                words[w] = 1

        counts = {'positive': 0, 'negative': 0}
        ratios = {'positive': 0, 'negative': 0}
        length_Tweet = len(words)

        for key in ['alexa', 'google']:
            if key in twt_Txt:
                for s in ['positive', 'negative']:
                    for i in sentiment_Dictionary[s].keys():
                        if i in words:
                            counts[s] += 1

                    ratios[s] = counts[s] / length_Tweet

                print '\t'.join([userId, key, str(ratios['positive'] - ratios['negative'])])


if __name__ == '__main__':
    main()