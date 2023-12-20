import numpy as np
import copy
import math
import functools

def get_lit(data,start):
    cur_tiles = [start]
    lit = {}
    checked_tiles = {}
    while len(cur_tiles):
        next_tiles = []
        for tile in cur_tiles:
            check_tile = [tile[0]+tile[2][0],tile[1]+tile[2][1]]
            if check_tile[0] < 0 or check_tile[0] >= len(data[0]) or check_tile[1] < 0 or check_tile[1] >= len(data):
                lit[tuple([tile[0],tile[1]])] = True
                continue
            if tuple(tile) in checked_tiles:
                continue
            checked_tiles[tuple(tile)] = True
            if data[check_tile[0]][check_tile[1]] == ".":
                next_tiles.append([check_tile[0],check_tile[1],tile[2]])
            elif data[check_tile[0]][check_tile[1]] == "/":
                if tuple(tile[2]) == tuple([0,1]):
                    next_tiles.append([check_tile[0],check_tile[1],tuple([-1,0])])
                elif tuple(tile[2]) == tuple([0,-1]):
                    next_tiles.append([check_tile[0],check_tile[1],tuple([1,0])])
                elif tuple(tile[2]) == tuple([1,0]):
                    next_tiles.append([check_tile[0],check_tile[1],tuple([0,-1])])
                else:
                    next_tiles.append([check_tile[0],check_tile[1],tuple([0,1])])
            elif data[check_tile[0]][check_tile[1]] == "\\":
                if tuple(tile[2]) == tuple([0,1]):
                    next_tiles.append([check_tile[0],check_tile[1],tuple([1,0])])
                elif tuple(tile[2]) == tuple([0,-1]):
                    next_tiles.append([check_tile[0],check_tile[1],tuple([-1,0])])
                elif tuple(tile[2]) == tuple([1,0]):
                    next_tiles.append([check_tile[0],check_tile[1],tuple([0,1])])
                else:
                    next_tiles.append([check_tile[0],check_tile[1],tuple([0,-1])])
            elif data[check_tile[0]][check_tile[1]] == "-":
                if tuple(tile[2]) == tuple([0,1]) or tuple(tile[2]) == tuple([0,-1]):
                    next_tiles.append([check_tile[0],check_tile[1],tile[2]])
                else:
                    next_tiles.append([check_tile[0],check_tile[1],tuple([0,1])])
                    next_tiles.append([check_tile[0],check_tile[1],tuple([0,-1])])
            elif data[check_tile[0]][check_tile[1]] == "|":
                if tuple(tile[2]) == tuple([1,0]) or tuple(tile[2]) == tuple([-1,0]):
                    next_tiles.append([check_tile[0],check_tile[1],tile[2]])
                else:
                    next_tiles.append([check_tile[0],check_tile[1],tuple([1,0])])
                    next_tiles.append([check_tile[0],check_tile[1],tuple([-1,0])])
            lit[tuple([tile[0],tile[1]])] = True
        cur_tiles = copy.deepcopy(next_tiles)
    return len(lit)-1
 

if __name__ == "__main__":
    sol1 = 0
    sol2 = 0
    with open("day16.txt") as f:
        data = f.read().split('\n')
    sol1 = get_lit(data,tuple([0,-1,tuple([0,1])]))

    for i in range(len(data)):
        tmp = get_lit(data,tuple([i,-1,tuple([0,1])]))
        if tmp > sol2:
            sol2 = tmp
        tmp = get_lit(data,tuple([i,len(data),tuple([0,-1])]))
        if tmp > sol2:
            sol2 = tmp
    for i in range(len(data[0])):
        tmp = get_lit(data,tuple([-1,i,tuple([1,0])]))
        if tmp > sol2:
            sol2 = tmp
        tmp = get_lit(data,tuple([len(data[0]),i,tuple([-1,0])]))
        if tmp > sol2:
            sol2 = tmp

    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
