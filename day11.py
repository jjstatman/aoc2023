import numpy as np
import math
import copy

def calc_dists(space, offset):
    galaxies = []
    output = 0
    i_offset = 0
    for i, line in enumerate(space):
        j_offset = 0
        if np.sum(line) == 0:
            i_offset += offset-1
        for j, char in enumerate(line):
            if np.sum(data[:,j]) == 0:
                j_offset += offset-1
            if char == 1:
                galaxies.append([i+i_offset,j+j_offset])
    for i, start in enumerate(galaxies):
        for end in galaxies[i+1:]:
            output += abs(start[0]-end[0]) + abs(start[1]-end[1])
    return output


if __name__ == "__main__":
    sol1 = 0
    sol2 = 0
    with open("day11.txt") as f:
        data = np.array([[1 if char == "#" else 0 for char in line] for line in f.read().split('\n') if line])
    
    print("Solution 1: ", calc_dists(data,2))
    print("Solution 2: ", calc_dists(data,1000000))

