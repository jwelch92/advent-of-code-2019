#!/usr/bin/env python3
# coding: utf-8

import os

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')

# 1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2)

OP_ADD = 1
OP_MUL = 2
OP_EX = 99

ops = {
    OP_ADD: lambda a, b: a + b,
    OP_MUL: lambda a, b: a * b,
}


def part1(data, noun, verb):
    # fix per instructions
    data[1] = noun
    data[2] = verb

    def get(arr, i, pos):
        return arr[arr[i + pos]]

    for i in range(0, len(data), 4):
        op_raw = data[i]
        if op_raw == OP_EX:
            break
        op = ops.get(op_raw)
        if op is not None:
            data[data[i + 3]] = op(get(data, i, 1), get(data, i, 2))
        else:
            print(f'bad opcode {op_raw} at {i}')

    return data


def part2(data, wanted):
    for i in range(0, 99):
        for j in range(0, 99):
            arr = data[:]
            result = part1(arr, i, j)
            if result[0] == wanted:
                return 100 * i + j


def main():
    with open(inputfile) as f:
        data = f.read()
    data = [int(x) for x in data.split(',')]

    # To do this, before running the program, replace position 1 with the value 12 and replace position 2 with the value 2. What value is left at position 0 after the program halts?

    print('result part1', part1(data[:], 12, 2)[0])
    print('result part2', part2(data[:], 19690720))


if __name__ == "__main__":
    main()
    # part1([1, 0, 0, 0, 99])
