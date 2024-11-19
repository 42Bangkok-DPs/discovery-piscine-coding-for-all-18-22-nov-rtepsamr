#!/usr/bin/env python3
import sys
sys.argv
def downcase_all(letters):
    return [letter.lower() for letter in letters]

letter = sys.argv[1:]

if len(sys.argv) == 1:
    print("none")
else:
    count = len(sys.argv[1:])
    for x in range(0,count):
        lowercased = downcase_all(letter)
        print(lowercased[x])