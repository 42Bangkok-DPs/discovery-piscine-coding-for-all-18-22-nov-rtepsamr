#!/usr/bin/env python3
def average(class_data):
    average_age = sum(class_data.values()) / len(class_data)
    return average_age

class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}
class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3B: {average(class_3C)}.")