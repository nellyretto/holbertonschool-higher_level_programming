#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
if number > 0 or last_digit == 0:
    print(f"Last Digit of {number} is {last_digit} ", end="")
else:
    print(f"Last digit of {number} is -{last_digit} ", end="")
if last_digit > 5 and number > 0:
    print(f"and is greater than 5")
elif last_digit == 0:
    print(f"and is 0")
else:
    print("and is less than 6 and not 0")
