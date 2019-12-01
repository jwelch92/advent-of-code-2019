#!/usr/bin/env python3
# coding: utf-8


import os


def slurp():
    dirname = os.path.dirname(__file__)
    inputfile = os.path.join(dirname, 'input.txt')
    with open(inputfile) as f:
        data = f.read().splitlines()
        data = map(int, data)
    return data


def calc_fuel(n):
    return (n // 3) - 2


def part1(data):
    return sum(map(calc_fuel, data))


def part2(data):
    total = 0
    for n in data:
        fuel = calc_fuel(n)
        total += fuel
        while True:
            fuel = calc_fuel(fuel)
            if fuel >= 0:
                total += fuel
            else:
                break
    return total


def main():
    data = slurp()
    print(part1(data))  # 3182375
    print(part2(data))  # 4770725


if __name__ == "__main__":
    main()
