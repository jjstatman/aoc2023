import numpy as np
import copy
import math
import functools

class Workflow:
    def __init__(self, raw):
        self.id = raw.split('{')[0]
        eqs = raw.split('{')[1][:-1].split(',')
        self.eqs = []
        for eq in raw.split('{')[1][:-1].split(','):
            tmp = eq.split(':')
            if len(tmp) > 1:
                if '>' in tmp[0]:
                    tmp2 = tmp[0].split('>')
                    self.eqs.append((tmp2[0],'>',int(tmp2[1]),tmp[1]))
                elif '<' in tmp[0]:
                    tmp2 = tmp[0].split('<')
                    self.eqs.append((tmp2[0],'<',int(tmp2[1]),tmp[1]))
            else:
                self.eqs.append(tuple(tmp))

    def getRating(self,obj,wfs,seen):
        out = ""
        for eq in self.eqs:
            if len(eq) == 1:
                out = eq[0]
            else:
                if eq[1] == '>':
                    if obj[eq[0]] > eq[2]:
                        out = eq[3]
                elif eq[1] == '<':
                    if obj[eq[0]] < eq[2]:
                        out = eq[3]
            if out == "R":
                return -1
            elif out == "A":
                return 1
            elif out and out in seen:
                print('sending to where i"ve seen')
            elif out:
                seen[self.id] = True
                return wfs[out].getRating(obj,wfs,seen)
        return 0

    def getSplits(self,splits,wfs,seen):
        counts = 0
        seen[self.id] = True
        for eq in self.eqs:
            if len(eq) == 1:
                if eq[0] == "A":
                    counts += (splits['x'][1]-splits['x'][0]+1)*(splits['m'][1]-splits['m'][0]+1)*(splits['a'][1]-splits['a'][0]+1)*(splits['s'][1]-splits['s'][0]+1)
                elif eq[0] == "R":
                    counts += 0
                else:
                    counts += wfs[eq[0]].getSplits(copy.deepcopy(splits),wfs,copy.deepcopy(seen))
                break
            else:
                if eq[1] == '>':
                    if splits[eq[0]][0] > eq[2]:
                        if eq[3] == "A":
                            counts += (splits['x'][1]-splits['x'][0]+1)*(splits['m'][1]-splits['m'][0]+1)*(splits['a'][1]-splits['a'][0]+1)*(splits['s'][1]-splits['s'][0]+1)
                        elif eq[3] == "R":
                            counts += 0
                        else:
                            counts += wfs[eq[3]].getSplits(copy.deepcopy(splits),wfs,copy.deepcopy(seen))
                    elif splits[eq[0]][1] < eq[2]:
                        continue
                    else:
                        if eq[3] == "A":
                            newsplits = copy.deepcopy(splits)
                            newsplits[eq[0]][0] = eq[2]+1
                            splits[eq[0]][1] = eq[2]
                            counts += (newsplits['x'][1]-newsplits['x'][0]+1)*(newsplits['m'][1]-newsplits['m'][0]+1)*(newsplits['a'][1]-newsplits['a'][0]+1)*(newsplits['s'][1]-newsplits['s'][0]+1)
                        elif eq[3] == "R":
                            splits[eq[0]][1] = eq[2]
                            counts += 0
                        else:
                            newsplits = copy.deepcopy(splits)
                            newsplits[eq[0]][0] = eq[2]+1
                            splits[eq[0]][1] = eq[2]
                            counts += wfs[eq[3]].getSplits(newsplits,wfs,copy.deepcopy(seen))
                elif eq[1] == "<":
                    if splits[eq[0]][1] < eq[2]:
                        if eq[3] == "A":
                            counts += (splits['x'][1]-splits['x'][0]+1)*(splits['m'][1]-splits['m'][0]+1)*(splits['a'][1]-splits['a'][0]+1)*(splits['s'][1]-splits['s'][0]+1)
                        elif eq[3] == "R":
                            counts += 0
                        else:
                            counts += wfs[eq[3]].getSplits(copy.deepcopy(splits),wfs,copy.deepcopy(seen))
                    elif splits[eq[0]][0] > eq[2]:
                        continue
                    else:
                        if eq[3] == "A":
                            newsplits = copy.deepcopy(splits)
                            newsplits[eq[0]][1] = eq[2]-1
                            splits[eq[0]][0] = eq[2]
                            counts += (newsplits['x'][1]-newsplits['x'][0]+1)*(newsplits['m'][1]-newsplits['m'][0]+1)*(newsplits['a'][1]-newsplits['a'][0]+1)*(newsplits['s'][1]-newsplits['s'][0]+1)
                        elif eq[3] == "R":
                            splits[eq[0]][0] = eq[2]
                            counts += 0
                        else:
                            newsplits = copy.deepcopy(splits)
                            newsplits[eq[0]][1] = eq[2]-1
                            splits[eq[0]][0] = eq[2]
                            counts += wfs[eq[3]].getSplits(newsplits,wfs,copy.deepcopy(seen))
        return counts





                    

if __name__ == "__main__":
    sol1 = 0
    sol2 = 0
    with open("day19.txt") as f:
        data = f.read().split('\n\n')

    wfs = {}
    for wf in data[0].split('\n'):
        if not wf:
            continue
        tmp = Workflow(wf)
        wfs[tmp.id] = copy.deepcopy(tmp)

    for item in data[1].split('\n'):
        if not item:
            continue
        tmp = {}
        ratings = item[1:-1].split(',')
        for rating in ratings:
            tmp2 = rating.split('=')
            tmp[tmp2[0]] = int(tmp2[1])
        if wfs["in"].getRating(tmp,wfs,{"in":True}) > 0:
            for key in tmp:
                sol1 += tmp[key]
    splits = {"x":[1,4000],"m":[1,4000],"a":[1,4000],"s":[1,4000]}
    sol2 = wfs["in"].getSplits(splits,wfs,{"in":True})


    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
