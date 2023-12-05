import numpy as np
import copy

def get_overlap(in_range, page):
    if in_range[1] <= page["from"]:
        return tuple([[], [[in_range[0],in_range[1]]]])
    elif in_range[0] >= page["from"] + page["range"]:
        return tuple([[], [[in_range[0],in_range[1]]]])
    elif in_range[0] >= page["from"] and in_range[1] <= page["from"] + page["range"]:
        return tuple([[page["to"] + in_range[0] - page["from"], page["to"] + in_range[1] - page["from"]], []])
    elif in_range[0] >= page["from"]:
        return tuple([[page["to"] + in_range[0] - page["from"], page["to"] + page["range"]], [[page["range"] + page["from"], in_range[1]]]])
    elif in_range[1] <= page["from"] + page["range"]:
        return tuple([[page["to"],page["to"] + in_range[1] - page["from"]], [[in_range[0],page["from"]]]])
    else:
        return tuple([[page["to"],page["to"]+page["range"]], [[in_range[0],page["from"]],[page["from"]+page["range"],in_range[1]]]])

def get_sections(in_range, section):
    curr_ranges = [copy.deepcopy(in_range)]
    next_ranges = copy.deepcopy(curr_ranges)
    ret = []
    for page in section:
        curr_ranges = copy.deepcopy(next_ranges)
        next_ranges = []
        for segment in curr_ranges:
            output = get_overlap(segment, page)
            for next_range in output[1]:
                next_ranges.append(copy.deepcopy(next_range))
            if len(output[0]):
                ret.append(output[0])
    for next_range in next_ranges:
        ret.append(next_range)
    return ret


if __name__ == "__main__":
    sol1 = 0
    sol2 = 0
    with open("day5.txt") as f:
        data = f.read().split('\n\n')
    seeds = [int(x) for x in data[0].split(': ')[1].split(' ')]
    ranges = []
    soils = []
    for section in data[1:]:
        ranges.append([])
        for page in section.split('\n')[1:]:
            vals = [int(x) for x in page.split(' ')]
            ranges[-1].append({"to":vals[0], "from":vals[1], "range":vals[2]})
    for seed in seeds:
        val = seed
        for i in range(len(ranges)):
            for page in ranges[i]:
                if val >= page["from"] and val < page["from"] + page["range"]:
                    val = page["to"] + val - page["from"]
                    print(val)
                    break
        soils.append(val)
    seed_ranges = []
    for i in range(int(len(seeds)/2)):
        in_range = [[seeds[2*i],seeds[2*i]+seeds[2*i+1]-1]]
        for i in range(len(ranges)):
            new_ranges = []
            for test in in_range:
                output = get_sections(test, ranges[i])
                for out_range in output:
                    new_ranges.append(out_range)
            in_range = copy.deepcopy(new_ranges)
        for seed_range in new_ranges:
            seed_ranges.append(seed_range)

    sol1 = min(soils)
    sol2 = seed_ranges[0][0]
    for fin_range in seed_ranges:
        if fin_range[0] < sol2:
            sol2 = fin_range[0]

    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
