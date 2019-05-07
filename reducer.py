#!/usr/bin/env python

from __future__ import division
# Importing all necessary modules
from operator import itemgetter
import sys
import csv

# Defining the reducer function
def main():
    alexa_average = 0.0
    alexa_tot = 0
    google_average = 0.0
    google_tot = 0
    for line in sys.stdin:
        line = line.strip()
        row = line.split('\t')
        key = row[1]
        avg = row[2]

        try:
            avg = float(avg)
        except:
            continue

        if key == 'alexa':
            alexa_average += avg
            alexa_tot += 1

        if key == 'google':
            google_average += avg
            google_tot += 1

    print ('Total avg score of products\n')
    print '%s\t%.4f' % ('alexa', alexa_average / alexa_tot)
    print '%s\t%.4f' % ('google', google_average / google_tot)


if __name__ == '__main__':
    main()
