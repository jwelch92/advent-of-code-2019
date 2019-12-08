#!/usr/bin/env python3
# coding: utf-8

import os

dirname = os.path.dirname(__file__)
inputfile = os.path.join(dirname, 'input.txt')

OP = {"L": (0, -1), "R": (0, 1), "U": (1, 1), "D": (1, -1)}


def part1(data):
    wires = []
    for line in data:
        wire = []
        cur_pos = [0, 0]
        for instr in line.split(","):
            for _ in range(int(instr[1:])):
                ops = OP.get(instr[0])
                cur_pos[ops[0]] += ops[1]
                wire.append(tuple(cur_pos))
        wires.append(wire)
    intersections = set(wires[0]) & set(wires[1])
    dist = min((abs(x) + abs(y) for x, y in intersections))
    print(dist)
    return wires, intersections


def part2(wires, intersections):
    p = 2 + min(sum(wire.index(intersect) for wire in wires) for intersect in intersections)
    print(p)
    return p


def main():
    with open(inputfile) as f:
        data = f.read().splitlines()
    wires, intersections = part1(data)
    part2(wires, intersections)


if __name__ == "__main__":
    main()
