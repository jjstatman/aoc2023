import numpy as np
import copy
import math
import functools

convert = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}

def parse_hand(hand):
    counts = []
    for i in range(2, 15):
        counts.append(hand.count(i))
    return counts

def parse_hand_2(hand):
    counts = []
    wilds = 0
    for i in range(2, 15):
        if not i == 11:
            counts.append(hand.count(i))
        else:
            wilds = hand.count(i)
            counts.append(0)
    counts[counts.index(max(counts))] += wilds

    return counts

def get_denom(hand):
    a = hand
    if max(a) == 5:
        return 1
    elif max(a) == 4:
        return 2
    elif max(a) == 3 and a.count(2) == 1:
        return 3
    elif max(a) == 3:
        return 4
    elif max(a) == 2 and a.count(2) == 2:
        return 5
    elif max(a) == 2:
        return 6
    else:
        return 7

def rank_hands(hand1, hand2):
    if get_denom(parse_hand(hand1[0])) > get_denom(parse_hand(hand2[0])):
        return 1
    elif get_denom(parse_hand(hand2[0])) > get_denom(parse_hand(hand1[0])):
        return -1
    else:
        for i in range(len(hand1[0])):
            if hand1[0][i] < hand2[0][i]:
                return 1
            elif hand2[0][i] < hand1[0][i]:
                return -1
    return 0

def rank_hands_2(hand1, hand2):
    if get_denom(parse_hand_2(hand1[0])) > get_denom(parse_hand_2(hand2[0])):
        return 1
    elif get_denom(parse_hand_2(hand2[0])) > get_denom(parse_hand_2(hand1[0])):
        return -1
    else:
        for i in range(len(hand1[0])):
            if hand1[0][i] < hand2[0][i]:
                if hand2[0][i] == 11:
                    return -1
                else:
                    return 1
            elif hand2[0][i] < hand1[0][i]:
                if hand1[0][i] == 11:
                    return 1
                else:
                    return -1
    return 0


if __name__ == "__main__":
    sol1 = 0
    sol2 = 0
    with open("day7.txt") as f:
        data = [[[convert[y] for y in x.split(' ')[0]], int(x.split(' ')[1])] for x in f.read().split('\n')]

    data.sort(key=functools.cmp_to_key(rank_hands), reverse=True)
    for i, hand in enumerate(data):
        sol1 += (i+1)*hand[1]
    data.sort(key=functools.cmp_to_key(rank_hands_2), reverse=True)
    for i, hand in enumerate(data):
        sol2 += (i+1)*hand[1]

    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
