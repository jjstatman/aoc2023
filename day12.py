import numpy as np
import copy
import math
import functools

def get_combos(line,pattern,used):
    oldline = line
    if tuple([line,pattern]) in used:
        return used[tuple([line,pattern])]
    while len(line) and line[0] == ".":
        line = line[1:]
    if line.count("#") + line.count("?") < sum(pattern):
        used[tuple([oldline,pattern])] = 0
        return 0
    if sum(pattern) + len(pattern) - 1 > len(line):
        used[tuple([oldline,pattern])] = 0
        return 0
    if len(pattern) == 0 and line.count("#") > 0:
        used[tuple([oldline,pattern])] = 0
        return 0
    if len(pattern) == 0 and line.count("#") == 0:
        used[tuple([oldline,pattern])] = 1
        return 1
    if line[0] == "#":
        for i in range(pattern[0]):
            if line[0] == "#" or line[0] == "?":
                line = line[1:]
                continue
            else:
                #val = get_combos(line,pattern,used)
                val = 0
                used[tuple([oldline,pattern])] = val
                return val
        if len(line) and line[0] == "#":
            used[tuple([oldline,pattern])] = 0
            return 0
        val = get_combos(line[1:],pattern[1:],used)
        used[tuple([oldline,pattern])] = val
        return val
    if line[0] == "?":
        val1 = get_combos(line[1:],pattern,used)
        for i in range(pattern[0]):
            if line[0] == "#" or line[0] == "?":
                line = line[1:]
                continue
            else:
                used[tuple([oldline,pattern])] = val1
                return val1
        if len(line) and line[0] == "#":
            used[tuple([oldline,pattern])] = val1
            return val1
        val2 = get_combos(line[1:],pattern[1:],used)
        used[tuple([oldline,pattern])] = val1 + val2
        return val1 + val2

if __name__ == "__main__":
    sol1 = 0
    sol2 = 0
    with open("day12.txt") as f:
        data = [[line.split(' ')[0], [int(x) for x in line.split(' ')[1].split(',')]] for line in f.read().split('\n')]
    used = {}
    for line in data:
        sol1 += get_combos(line[0], tuple(line[1]), used)
        sol2 += get_combos(line[0]+"?"+line[0]+"?"+line[0]+"?"+line[0]+"?"+line[0], tuple(line[1])+tuple(line[1])+tuple(line[1])+tuple(line[1])+tuple(line[1]), used)
        print(used[tuple([line[0], tuple(line[1])])])

    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
