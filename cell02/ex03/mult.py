#!/usr/bin/env python3
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
result = x * y
print(result)
if result > 0:
    print(x,"X",y,"=",result)
    print("The result is positive.")
elif result == 0:
    print(x,"X",y,"=",result)
    print("The result is both positive and negative.")
else:
    print(x,"X",y,"=",result)
    print("The result is negative.")