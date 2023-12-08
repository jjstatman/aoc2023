import numpy as np
import copy
import math
import functools

class Node:
    def __init__(self, raw):
        self.id = raw.split(' = ')[0]
        self.left = raw.split('(')[1].split(',')[0]
        self.right = raw.split(', ')[1].split(')')[0]

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

if __name__ == "__main__":
    sol1 = 0
    sol2 = 0
    with open("day8.txt") as f:
        (turns, raw_nodes) = f.read().split('\n\n')

    nodes = {}
    part2_starts = []
    part2_ends = []
    for line in raw_nodes.split('\n'):
        tmp = Node(line)
        nodes[tmp.id] = tmp
        if tmp.id[-1] == "A":
            part2_starts.append(tmp.id)
        if tmp.id[-1] == "Z":
            part2_ends.append(tmp.id)

    cur_node = "AAA"
    i = 0
    while not cur_node == "ZZZ":
        if turns[i % len(turns)] == "L":
            cur_node = nodes[cur_node].left
        else:
            cur_node = nodes[cur_node].right
        i += 1
    sol1 = i

    num_turns = []

    for start_node in (part2_starts):
        cur_node = start_node
        i = 0
        found_ends = []
        saved = {}
        steady = False
        while not steady:
            if turns[i % len(turns)] == "L":
                cur_node = nodes[cur_node].left
            else:
                cur_node = nodes[cur_node].right
            i += 1
            if cur_node in part2_ends:
                if not (cur_node,(i%len(turns))) in found_ends:
                    found_ends.append(tuple([cur_node,(i%len(turns))]))
                    saved[found_ends[-1]] = i
                else:
                    saved["looper"] = (cur_node, i % len(turns))
                    saved["period"] = i - saved[(cur_node, i%len(turns))]
                    num_turns.append(saved)
                    steady = True
    sol2 = 1
    for start in num_turns:
        sol2 = lcm(sol2,start['period'])
            
    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
