import numpy as np
import copy
import math

def get_ways(time,dist):
    max_t = math.floor(time/2.0 + math.sqrt(time*time - 4*dist)/2.0)
    min_t = math.ceil(time/2.0 - math.sqrt(time*time - 4*dist)/2.0)
    return max_t - min_t + 1

if __name__ == "__main__":
    sol1 = 1
    sol2 = 0
    with open("day6.txt") as f:
        data = f.read().split('\n')
    times = [int(x) for x in data[0].split(' ')[1:] if x]
    dists = [int(x) for x in data[1].split(' ')[1:] if x]

    for i in range(len(times)):
        sol1 *= get_ways(times[i], dists[i])

    time = ""
    dist = ""
    for time_part in times:
        time += str(time_part)
    time = int(time)
    for dist_part in dists:
        dist += str(dist_part)
    dist = int(dist)
    sol2 = get_ways(time,dist)


    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
