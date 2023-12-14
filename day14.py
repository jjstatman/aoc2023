import numpy as np
import copy
import math
import functools

convert = {"O": 1, ".": 0, "#": -1}

def tilt_north(data):
    for i, row in enumerate(data[1:]):
        for j, tile in enumerate(row):
            if tile == 1 and data[i,j] == 0:
                ind = i
                while ind > 0 and data[ind,j] == 0:
                    if data[ind-1,j] == 0:
                        ind -= 1
                    else:
                        break
                data[ind,j] = 1
                data[i+1,j] = 0

def tilt_west(data):
    data = data.T
    for i, row in enumerate(data[1:]):
        for j, tile in enumerate(row):
            if tile == 1 and data[i,j] == 0:
                ind = i
                while ind > 0 and data[ind,j] == 0:
                    if data[ind-1,j] == 0:
                        ind -= 1
                    else:
                        break
                data[ind,j] = 1
                data[i+1,j] = 0
    data = data.T

def tilt_south(data):
    data = np.flipud(data)
    for i, row in enumerate(data[1:]):
        for j, tile in enumerate(row):
            if tile == 1 and data[i,j] == 0:
                ind = i
                while ind > 0 and data[ind,j] == 0:
                    if data[ind-1,j] == 0:
                        ind -= 1
                    else:
                        break
                data[ind,j] = 1
                data[i+1,j] = 0
    data = np.flipud(data)

def tilt_east(data):
    data = np.flipud(data.T)
    for i, row in enumerate(data[1:]):
        for j, tile in enumerate(row):
            if tile == 1 and data[i,j] == 0:
                ind = i
                while ind > 0 and data[ind,j] == 0:
                    if data[ind-1,j] == 0:
                        ind -= 1
                    else:
                        break
                data[ind,j] = 1
                data[i+1,j] = 0
    data = np.flipud(data).T

def get_weight(data):
    ret = 0
    counter = 0
    for row in data:
        unique, counts = np.unique(row, return_counts=True)
        if 1 in unique:
            ret += (len(data)-counter)*dict(zip(unique,counts))[1]
        counter += 1
    return ret

def convert_number(data):
    ret = []
    for row in data:
        ret.append(np.sum(np.power(2.0, row)))
    return tuple(ret)

past_cycles = {}

if __name__ == "__main__":
    sol1 = 0
    sol2 = 0
    with open("day14.txt") as f:
        data = np.array([[convert[x] for x in line] for line in f.read().split('\n')])
    for i in range(1000000000):
        tilt_north(data)
        if i == 0:
            sol1 = get_weight(data)
        tilt_west(data)
        tilt_south(data)
        tilt_east(data)
        checkval = convert_number(data)
        if checkval in past_cycles:
            cycle = i - past_cycles[checkval]
            goal = (1000000000 - i-1) % cycle
            for i in range(goal):
                tilt_north(data)
                tilt_west(data)
                tilt_south(data)
                tilt_east(data)
            break
        past_cycles[checkval] = i
    sol2 = get_weight(data)

    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
