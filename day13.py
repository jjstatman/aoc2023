import numpy as np
import copy
import math
import functools

convert = {"#": 1, ".": 0}

if __name__ == "__main__":
    sol1 = 0
    sol2 = 0
    with open("day13.txt") as f:
        data = [np.array([[convert[x] for x in line] for line in maps.split('\n')]) for maps in f.read().split('\n\n') if maps]
    for rockmap in data:
        for i in range(len(rockmap)-1):
            c_ind_1 = i
            c_ind_2 = i+1
            found_reflect = True
            while c_ind_1 >= 0 and c_ind_2 < len(rockmap):
                if not np.sum(np.abs(rockmap[c_ind_1,:] - rockmap[c_ind_2,:])) == 0:
                    found_reflect = False
                    break
                c_ind_1 -= 1
                c_ind_2 += 1
            if found_reflect:
                sol1 += 100*(i+1)
                break
        if not found_reflect:
            for i in range(len(rockmap[0])-1):
                c_ind_1 = i
                c_ind_2 = i+1
                found_reflect = True
                while c_ind_1 >= 0 and c_ind_2 < len(rockmap[0]):
                    if not np.sum(np.abs(rockmap[:,c_ind_1] - rockmap[:,c_ind_2])) == 0:
                        found_reflect = False
                        break
                    c_ind_1 -= 1
                    c_ind_2 += 1
                if found_reflect:
                    sol1 += i+1
                    break
    for rockmap in data:
        for i in range(len(rockmap)-1):
            c_ind_1 = i
            c_ind_2 = i+1
            used_flip = False
            found_reflect = True
            while c_ind_1 >= 0 and c_ind_2 < len(rockmap):
                if np.sum(np.abs(rockmap[c_ind_1,:]-rockmap[c_ind_2,:])) == 0:
                    c_ind_1 -= 1
                    c_ind_2 += 1
                    continue
                elif np.sum(np.abs(rockmap[c_ind_1,:]-rockmap[c_ind_2,:])) == 1 and not used_flip:
                    c_ind_1 -= 1
                    c_ind_2 += 1
                    used_flip = True
                    continue
                else:
                    found_reflect = False
                    break
            if found_reflect and used_flip:
                sol2 += 100*(i+1)
                break
        if not found_reflect or not used_flip:
            for i in range(len(rockmap[0])-1):
                c_ind_1 = i
                c_ind_2 = i+1
                found_reflect = True
                used_flip = False
                while c_ind_1 >=0 and c_ind_2 < len(rockmap[0]):
                    if np.sum(np.abs(rockmap[:,c_ind_1]-rockmap[:,c_ind_2])) == 0:
                        c_ind_1 -= 1
                        c_ind_2 += 1
                        continue
                    elif np.sum(np.abs(rockmap[:,c_ind_1]-rockmap[:,c_ind_2])) == 1 and not used_flip:
                        c_ind_1 -= 1
                        c_ind_2 += 1
                        used_flip = True
                        continue
                    else:
                        found_reflect = False
                        break
                if found_reflect and used_flip:
                    sol2 += i+1
                    break

    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
