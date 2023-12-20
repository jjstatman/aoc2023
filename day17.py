import numpy as np
import math
import copy

dirs = np.array([[1,0],[-1,0],[0,1],[0,-1]])
switch_dir = {"ew":"ns", "ns":"ew"}

def get_costs(node,data,last_dir):
    out = []
    pos_val = 0
    neg_val = 0
    for i in range(1,4):
        if last_dir == 'ns':
            next_node1 = (node[0] + i*1, node[1])
            next_node2 = (node[0] - i*1, node[1])
            if next_node1[0] >= 0 and next_node1[0] < len(data) and next_node1[1] >= 0 and next_node1[1] < len(data[0]):
                pos_val += data[next_node1[0]][next_node1[1]]
                out.append(tuple([next_node1[0],next_node1[1],pos_val]))
            if next_node2[0] >= 0 and next_node2[0] < len(data) and next_node2[1] >= 0 and next_node2[1] < len(data[0]):
                neg_val += data[next_node2[0]][next_node2[1]]
                out.append(tuple([next_node2[0],next_node2[1],neg_val]))
        elif last_dir == 'ew':
            next_node1 = (node[0], node[1] + i*1)
            next_node2 = (node[0], node[1] - i*1)
            if next_node1[0] >= 0 and next_node1[0] < len(data) and next_node1[1] >= 0 and next_node1[1] < len(data[0]):
                pos_val += data[next_node1[0]][next_node1[1]]
                out.append(tuple([next_node1[0],next_node1[1],pos_val]))
            if next_node2[0] >= 0 and next_node2[0] < len(data) and next_node2[1] >= 0 and next_node2[1] < len(data[0]):
                neg_val += data[next_node2[0]][next_node2[1]]
                out.append(tuple([next_node2[0],next_node2[1],neg_val]))
    return out

def get_costs_2(node,data,last_dir):
    out = []
    pos_val = 0
    neg_val = 0
    for i in range(1,11):
        if last_dir == 'ns':
            next_node1 = (node[0] + i*1, node[1])
            next_node2 = (node[0] - i*1, node[1])
            if next_node1[0] >= 0 and next_node1[0] < len(data) and next_node1[1] >= 0 and next_node1[1] < len(data[0]):
                pos_val += data[next_node1[0]][next_node1[1]]
                if i >= 4:
                    out.append(tuple([next_node1[0],next_node1[1],pos_val]))
            if next_node2[0] >= 0 and next_node2[0] < len(data) and next_node2[1] >= 0 and next_node2[1] < len(data[0]):
                neg_val += data[next_node2[0]][next_node2[1]]
                if i >= 4:
                    out.append(tuple([next_node2[0],next_node2[1],neg_val]))
        elif last_dir == 'ew':
            next_node1 = (node[0], node[1] + i*1)
            next_node2 = (node[0], node[1] - i*1)
            if next_node1[0] >= 0 and next_node1[0] < len(data) and next_node1[1] >= 0 and next_node1[1] < len(data[0]):
                pos_val += data[next_node1[0]][next_node1[1]]
                if i >= 4:
                    out.append(tuple([next_node1[0],next_node1[1],pos_val]))
            if next_node2[0] >= 0 and next_node2[0] < len(data) and next_node2[1] >= 0 and next_node2[1] < len(data[0]):
                neg_val += data[next_node2[0]][next_node2[1]]
                if i >= 4:
                    out.append(tuple([next_node2[0],next_node2[1],neg_val]))
    return out

if __name__ == "__main__":
    sol1 = 0
    sol2 = 0
    with open("day17.txt") as f:
        data = np.array([[int(x) for x in line] for line in f.read().split('\n') if line])

    costs = {}
    checks = {}
    checks[tuple([len(data)-1,len(data[0])-1,'ns'])] = data[-1,-1]
    checks[tuple([len(data)-1,len(data[0])-1,'ew'])] = data[-1,-1]
    while(len(checks)):
        next_checks = {}
        for check in checks:
            tmp_costs = get_costs((check[0],check[1]),data,check[2])
            for cost in tmp_costs:
                if (cost[0],cost[1],switch_dir[check[2]]) in costs:
                    if costs[(cost[0],cost[1],switch_dir[check[2]])] <= cost[2]+checks[check]:
                        continue
                costs[(cost[0],cost[1],switch_dir[check[2]])] = cost[2] + checks[check]
                next_checks[(cost[0],cost[1],switch_dir[check[2]])] = cost[2]+checks[check]
        checks = copy.deepcopy(next_checks)
    sol1 = min(costs[(0,0,'ns')],costs[(0,0,'ew')]) - data[0,0]

    costs = {}
    checks = {}
    checks[tuple([len(data)-1,len(data[0])-1,'ns'])] = data[-1,-1]
    checks[tuple([len(data)-1,len(data[0])-1,'ew'])] = data[-1,-1]
    while(len(checks)):
        next_checks = {}
        for check in checks:
            tmp_costs = get_costs_2((check[0],check[1]),data,check[2])
            for cost in tmp_costs:
                if (cost[0],cost[1],switch_dir[check[2]]) in costs:
                    if costs[(cost[0],cost[1],switch_dir[check[2]])] <= cost[2]+checks[check]:
                        continue
                costs[(cost[0],cost[1],switch_dir[check[2]])] = cost[2] + checks[check]
                next_checks[(cost[0],cost[1],switch_dir[check[2]])] = cost[2]+checks[check]
        checks = copy.deepcopy(next_checks)
    sol2 = min(costs[(0,0,'ns')],costs[(0,0,'ew')]) - data[0,0]
        
    
    print("Solution 1: ", sol1)
    print("Solution 2: ", sol2)

