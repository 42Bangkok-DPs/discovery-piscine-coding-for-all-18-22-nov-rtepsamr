#!/usr/bin/env python3
import sys
argument = sys.argv
i = len(argument)
if i == 1:
    print("none")
elif i == 2:
    first_word = sys.argv[1]
    second_word = input("What was the parameter? ")
    print("Good jobs!")
else:
    print("Nope, sorry...")
