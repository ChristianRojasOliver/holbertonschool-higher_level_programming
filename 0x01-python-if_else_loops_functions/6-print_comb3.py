#!/usr/bin/python3
for a in range(0, 90):
    if a != 89:
        if a // 10 < a % 10:
            print("{:02d}".format(a), end=", ")
    else:
        print("{:02d}".format(a))
