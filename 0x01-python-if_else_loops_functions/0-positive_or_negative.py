#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if (number > 0):
    print(f"{number} positive")
elif (number == 0):
    print(f"{number} zero")
elif (number < 0):
    print(f"{number}  negative")
