import numpy as np
import copy
import math
import functools

def get_hash(command):
    value = 0
    for char in command:
        value += ord(char)
        value = (value*17) % 256
    return value

boxes = {}

if __name__ == "__main__":
    sol1 = 0
    sol2 = 0
    with open("day15.txt") as f:
        data = f.read().split(',')
    for command in data:
        sol1 += get_hash(command)
        if '=' in command:
            label, flen = command.split('=')
            box = get_hash(label)
            if not box in boxes:
                boxes[box] = [(label, flen)]
            else:
                replace = False
                for i, lens in enumerate(boxes[box]):
                    if lens[0] == label:
                        replace = True
                        break
                if replace:
                    boxes[box][i] = (label, flen)
                else:
                    boxes[box].append(tuple([label,flen]))
        elif '-' in command:
            label = command.split('-')[0]
            box = get_hash(label)
            if box in boxes:
                delete = False
                for i, lens in enumerate(boxes[box]):
                    if lens[0] == label:
                        delete = True
                        break
                if delete:
                    boxes[box].pop(i)
    for box in boxes:
        for i, lens in enumerate(boxes[box]):
            sol2 += (1+box)*(i+1)*int(lens[1])



    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
