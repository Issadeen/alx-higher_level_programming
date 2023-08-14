#!/usr/bin/python3
from sys import argv

argc = len(argv) - 1
if argc == 0:
    print("0 arguments.")
else:
    if argc == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(argc))

    for i, arg in enumerate(argv[1:], start=1):
        print("{:d}: {}".format(i, arg))
