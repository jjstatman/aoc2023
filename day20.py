import numpy as np
import copy
import math
import functools

class Module():
    def __init__(self, raw):
        if raw[0] == "%":
            self.type = "flip-flop"
            self.id = raw.split(' -> ')[0][1:]
            self.state = 0
        elif raw[0] == "&":
            self.type = "conj"
            self.id = raw.split(' -> ')[0][1:]
        else:
            self.type = "broadcast"
            self.id = "broadcast"
        self.outputs = raw.split(' -> ')[1].split(', ')
        self.inputs = []
        self.states = []
        self.counts = [0,0]
    
    def add_input(self,module):
        self.inputs.append(module)
        if self.type == "conj":
            self.states.append(0)

    def processPulse(self,pulse):
        out = []
        self.counts[pulse[1]] += 1
        if self.type == "broadcast":
            for mod in self.outputs:
                out.append((mod, pulse[1], self.id))
            return out
        elif self.type == "flip-flop":
            if pulse[1] == 0:
                if self.state == 0:
                    self.state = 1
                else:
                    self.state = 0
                for mod in self.outputs:
                    out.append((mod,self.state,self.id))
            return out

        elif self.type == "conj":
            ind = self.inputs.index(pulse[2])
            self.states[ind] = pulse[1]
            if np.prod(self.states) == 1:
                for mod in self.outputs:
                    out.append((mod, 0, self.id))
            else:
                for mod in self.outputs:
                    out.append((mod, 1, self.id))
            return out

if __name__ == "__main__":
    sol1 = 0
    sol2 = 0
    with open("day20.txt") as f:
        data = f.read().split('\n')
    mods = {}
    for mod in data:
        tmp = Module(mod)
        mods[tmp.id] = copy.deepcopy(tmp)

    outputs = {}

    for key in mods:
        for out in mods[key].outputs:
            if out in mods:
                mods[out].add_input(key)
            else:
                if out == "rx":
                    rx_in = key
                outputs[out] = [0,0]
    #for i in range(1000):
    i = 0
    cycle_1 = 0
    cycle_2 = 0
    cycle_3 = 0
    cycle_4 = 0
    while not cycle_1 or not cycle_2 or not cycle_3 or not cycle_4 or i < 1000:
        pulses = [("broadcast", 0, [])]
        while len(pulses):
            new_pulses = []
            for pulse in pulses:
                if pulse[0] in mods:
                    for n_pulse in mods[pulse[0]].processPulse(pulse):
                        new_pulses.append(n_pulse)
                else:
                    outputs[pulse[0]][pulse[1]] += 1
            if not cycle_1 and np.prod(mods[mods[mods[rx_in].inputs[0]].inputs[0]].states) == 1:
                cycle_1 = i+1
            if not cycle_2 and np.prod(mods[mods[mods[rx_in].inputs[1]].inputs[0]].states) == 1:
                cycle_2 = i+1
            if not cycle_3 and np.prod(mods[mods[mods[rx_in].inputs[2]].inputs[0]].states) == 1:
                cycle_3 = i+1
            if not cycle_4 and np.prod(mods[mods[mods[rx_in].inputs[3]].inputs[0]].states) == 1:
                cycle_4 = i+1
            pulses = copy.deepcopy(new_pulses)
        i += 1
        if i == 1000:
            tot_counts = [0,0]
            for mod in mods:
                tot_counts[0] += mods[mod].counts[0]
                tot_counts[1] += mods[mod].counts[1]
            for output in outputs:
                tot_counts[0] += outputs[output][0]
                tot_counts[1] += outputs[output][1]

            sol1 = tot_counts[0]*tot_counts[1]

    gcd = np.gcd(np.gcd(np.gcd(cycle_1,cycle_2),cycle_3),cycle_4)
    sol2 = int(cycle_1*cycle_2*cycle_3*cycle_4/gcd)



    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
