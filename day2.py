import numpy as np

if __name__ == "__main__":
    sol1 = 0
    sol2 = 0
    cubes = {"red": 12, "green": 13, "blue": 14}
    with open("day2.txt") as f:
        for line in f.read().split('\n'):
            gameID = int(line.split(':')[0].split(' ')[1])
            turns = line.split(':')[1].split(';')
            valid = True
            min_colors = {"red": 0, "green": 0, "blue": 0}
            for turn in turns:
                for color in turn.split(','):
                    num, c = color.strip().split(' ')
                    if int(num) > cubes[c]:
                        valid = False
                    if int(num) > min_colors[c]:
                        min_colors[c] = int(num)
            if valid == True:
                sol1 += gameID
            sol2 += min_colors["red"]*min_colors["blue"]*min_colors["green"]

    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
