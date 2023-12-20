import numpy as np
import math
import copy

dirs = {"R": np.array((0,1)), "L": np.array((0,-1)), "U": np.array((-1,0)), "D": np.array((1,0))}
dirs2 = {"0":"R","1":"D","2":"L","3":"U"}

def get_area(segments):
    out = 0
    cur_point = np.array([0,0])
    points = [copy.deepcopy(cur_point)]
    for segment in segments:
       tmp = cur_point + segment[1]*dirs[segment[0]]
       cur_point = copy.deepcopy(tmp)
       points.append(tmp)
    for i, point in enumerate(points):
        out += point[0]*points[(i+1) % len(points)][1]
        out -= point[1]*points[(i+1) % len(points)][0]
    out = abs(out)/2
    pos_sign = 0
    neg_sign = 0
    for i, segment in enumerate(segments):
        sign = np.cross(dirs[segment[0]],dirs[segments[(i+1)%len(segments)][0]])
        if sign > 0:
            pos_sign += 1
        else:
            neg_sign += 1
    total_angle = (len(segments)-2)*180
    if (total_angle - len(segments)*90)/180 == pos_sign:
        #positive cross product is inside
    	inside_cross = 1
    else:
        #negative cross product is inside
    	inside_cross = -1
    for i, segment in enumerate(segments):
        sign = np.cross(dirs[segment[0]],dirs[segments[(i+1)%len(segments)][0]])
        if sign == inside_cross:
            out += 0.25
        else:
            out += 0.75
        out += (segment[1]-1)/2.0
    return int(out)
 

if __name__ == "__main__":
    sol1 = 0
    sol2 = 0
    with open("day18.txt") as f:
        data = [line.split(' ') for line in f.read().split('\n') if line]
    segments = []
    cur_point = np.array([0,0])
    for command in data:
       segments.append((command[0],int(command[1])))
    sol1 = get_area(segments)
    segments2 = []
    for command in data:
        segments2.append((dirs2[command[2][-2]],int(command[2][2:-2],16)))
    sol2 = get_area(segments2)
        
            
    print("Solution 1: ", sol1)
    print("Solution 2: ", sol2)

