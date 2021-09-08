#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
msg = "Last digit of {} is {} "
great = "and is greater than 5"
zero = "and is 0"
less = "and is less than 6 and not 0"
last_digit = abs(number) % 10

if number < 0:
    last_digit = last_digit * -1

if last_digit > 5:
    print(msg.format(number, last_digit) + great)
elif last_digit == 0:
    print(msg.format(number, last_digit) + zero)
else:
    print(msg.format(number, last_digit) + less)
