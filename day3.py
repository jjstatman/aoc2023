import numpy as np

if __name__ == "__main__":
    sol1 = 0
    sol2 = 0
    nums = []
    chars = {}
    parts = []
    with open("day3.txt") as f:
        for i, line in enumerate(f.read().split('\n')):
            curnum = ''
            for j, char in enumerate(line):
                if char.isdigit():
                    curnum += char
                elif len(curnum) > 0:
                    nums.append({"val":int(curnum),"row":i,"cols":[j-len(curnum),j-1]})
                    curnum = ''
                    if not char == '.':
                        chars[(i,j)] = char
                elif char == '.':
                    continue
                else:
                    chars[(i,j)] = char
            if len(curnum) > 0:
                nums.append({"val":int(curnum),"row":i,"cols":[len(line)-len(curnum),len(line)-1]})

    gears = {}
    for num in nums:
        adjacent = False
        check = (num["row"], num["cols"][0]-1)
        if check in chars:
            adjacent = True
            if chars[check] == "*":
                if check in gears:
                    gears[check].append(num["val"])
                else:
                    gears[check] = [num["val"]]
        check = (num["row"], num["cols"][1]+1)
        if check in chars:
            adjacent = True
            if chars[check] == "*":
                if check in gears:
                    gears[check].append(num["val"])
                else:
                    gears[check] = [num["val"]]
        for k in range(num["cols"][0]-1,num["cols"][1]+2):
            check = (num["row"]-1, k)
            if check in chars:
                adjacent = True
                if chars[check] == "*":
                    if check in gears:
                        gears[check].append(num["val"])
                    else:
                        gears[check] = [num["val"]]
            check = (num["row"]+1, k)
            if check in chars:
                adjacent = True
                if chars[check] == "*":
                    if check in gears:
                        gears[check].append(num["val"])
                    else:
                        gears[check] = [num["val"]]
        if adjacent:
            parts.append(num["val"])
            continue
    sol1 = sum(parts)
    for key in gears:
        gear = gears[key]
        if len(gear) == 2:
            sol2 += gear[0]*gear[1]

    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
