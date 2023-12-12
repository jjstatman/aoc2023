import numpy as np
import math
import copy

convert = {"|": [0,2], "-": [1,3], "L": [0,1], "J": [0,3], "7": [2,3], "F": [2,1], ".": [], "S": "*"}
dirs = [0,1,2,3]
oppdirs = {0:2,1:3,2:0,3:1}
dirdelta = {0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}

if __name__ == "__main__":
    sol1 = 0
    sol2 = 0
    pipemap = {}
    with open("day10.txt") as f:
        data = [line for line in f.read().split('\n') if line]
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            pipemap[(i,j)] = convert[char]
            if char == "S":
               startloc = np.array((i,j))
    foundloop = False
    for startdir in dirs:
        looplen = 0
        curr_loc = startloc
        nextloc = startloc + dirdelta[startdir]
        nextdir = oppdirs[startdir]
        inpipe = True
        loop = [tuple(startloc)]
        start_shape = [startdir]
        while tuple(nextloc) in pipemap and inpipe:
            if np.all(nextloc == startloc):
                foundloop = True
                loop.append(tuple(startloc))
                start_shape.append(nextdir)
                break
            if nextdir in pipemap[tuple(nextloc)]:
                nextdirs = pipemap[tuple(nextloc)]
                for j in range(len(nextdirs)):
                    if not nextdir == nextdirs[j]:
                        loop.append(tuple(nextloc))
                        nextdir = oppdirs[nextdirs[j]]
                        nextloc = nextloc + dirdelta[nextdirs[j]]
                        looplen += 1
                        break
            else:
                inpipe = False
        if foundloop == True:
            sol1 = (looplen+1)//2
            break
    side1 = []
    side2 = []
    side1dir = []
    for i, pipe  in enumerate(loop[:-1]):
        if pipemap[pipe] == [0,2] or pipemap[pipe] == [1,3]:
            if side1dir == []:
                if pipemap[pipe] == [0,2]:
                    side1dir = np.array([0,1])
                    side2dir = np.array([0,-1])
                else:
                    side1dir = np.array([1,0])
                    side2dir = np.array([-1,0])
            side1loc = tuple(side1dir + pipe)
            side2loc = tuple(side2dir + pipe)
            if side1loc in pipemap and not side1loc in loop and not side1loc in side1:
                side1.append(side1loc)
            if side2loc in pipemap and not side2loc in loop and not side2loc in side2:
                side2.append(side2loc)
        else:
            if len(side1dir):
                side1loc = tuple(side1dir + pipe)
                side2loc = tuple(side2dir + pipe)
                if side1loc in pipemap and not side1loc in loop and not side1loc in side1:
                    side1.append(side1loc)
                if side2loc in pipemap and not side2loc in loop and not side2loc in side2:
                    side2.append(side2loc)
                if np.cross(np.array(loop[i])-np.array(loop[i-1]),np.array(loop[i+1]) - np.array(loop[i])) > 0:
                    side1dir = np.dot(side1dir, np.array([[0,1],[-1,0]]))
                    side2dir = np.dot(side2dir, np.array([[0,1],[-1,0]]))
                else:
                    side1dir = np.dot(side1dir, np.array([[0,-1],[1,0]]))
                    side2dir = np.dot(side2dir, np.array([[0,-1],[1,0]]))
                side1loc = tuple(side1dir + pipe)
                side2loc = tuple(side2dir + pipe)
                if side1loc in pipemap and not side1loc in loop and not side1loc in side1:
                    side1.append(side1loc)
                if side2loc in pipemap and not side2loc in loop and not side2loc in side2:
                    side2.append(side2loc)
    lastside1 = []
    outside = False
    while not len(lastside1) == len(side1) and not outside:
        lastside1 = copy.deepcopy(side1)
        for tile in lastside1:
            for checkdir in dirs:
                checkloc = tuple(np.array(tile) + dirdelta[checkdir])
                if checkloc[0] == 0 or checkloc[0] == len(data)-1 or checkloc[1] == 0 or checkloc[1] == len(data[0])-1:
                    outside = True
                if checkloc in pipemap and not checkloc in loop and not checkloc in side1:
                    side1.append(checkloc)
    if not outside:
        sol2 = len(side1)
    lastside2 = []
    while not len(lastside2) == len(side2) and outside:
        lastside2 = copy.deepcopy(side2)
        for tile in lastside2:
            for checkdir in dirs:
                checkloc = tuple(np.array(tile) + dirdelta[checkdir])
                if checkloc in pipemap and not checkloc in loop and not checkloc in side2:
                    side2.append(checkloc)
    if outside:
        sol2 = len(side2)

    
    print("Solution 1: ", sol1)
    print("Solution 2: ", sol2)

