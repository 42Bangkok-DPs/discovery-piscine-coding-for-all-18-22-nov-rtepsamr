#!/usr/bin/env python3
def greetings(name=None):
    if isinstance(name, str) == True:
        return print(f"Hello, {name}")
    elif name is None:
        return print(f"Hello, noble stranger")
    else:
        return print("Error! It was not a name.")
greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)