#!/usr/bin/env python3
# coding: utf-8

import os
from collections import Counter

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')


def check_double(n):
    return any(x > 1 for x in Counter(str(n)).values())


def check_only_double(n):
    return any(x == 2 for x in Counter(str(n)).values())


def check_increasing(n):
    c = "0"
    for x in list(str(n)):
        if int(x) < int(c):
            return False
        c = x
    return True


def part1(data):
    pwds = []
    for x in range(*data):
        if check_double(x) and check_increasing(x):
            pwds.append(x)

    print("PART 1")
    print(len(pwds))


def part2(data):
    pwds = []
    for x in range(*data):
        if check_only_double(x) and check_increasing(x):
            pwds.append(x)

    print("PART 2")
    print(len(pwds))


def main():
    data = "256310-732736"
    rg = [int(x) for x in data.split("-")]
    part1(rg)
    part2(rg)


if __name__ == "__main__":
    main()
