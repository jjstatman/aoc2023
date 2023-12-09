import numpy as np
import copy
import math
import functools

def get_next(line):
    next_line = []
    for i in range(len(line)-1):
        next_line.append(line[i+1]-line[i])
    return next_line

if __name__ == "__main__":
    sol1 = 0
    sol2 = 0
    with open("day9.txt") as f:
        data = [[int(x) for x in line.split(' ')] for line in f.read().split('\n')]

    for line in data:
        lines = {}
        i = 0
        cur_line = line
        converged = False
        lines[i] = line
        while not converged:
            next_line = get_next(cur_line)
            i += 1
            lines[i] = next_line
            cur_line = copy.deepcopy(next_line)
            converged = True
            for num in cur_line:
                if num:
                    converged = False
        val = 0
        for j in range(i,-1,-1):
            sol1 += lines[j][-1]
            val = lines[j][0] - val
        sol2 += val

    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
