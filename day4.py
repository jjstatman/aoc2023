import numpy as np

if __name__ == "__main__":
    sol1 = 0
    sol2 = 0
    cardwins = []
    with open("day4.txt") as f:
        for line in f.read().split('\n'):
            cardnum = int(line.split(':')[0].split(' ')[-1])
            numbers = line.split(':')[1].strip().split('|')
            print(numbers)
            wins = [int(x) for x in numbers[0].strip().split(' ') if x or x == "0"]
            scratch = [int(x) for x in numbers[1].strip().split(' ') if x or x == "0"]
            count = 0
            for num in wins:
                if num in scratch:
                    count += 1
            if count:
                sol1 += pow(2,count-1)
            cardwins.append(count)
    cards = np.ones(len(cardwins),dtype=int)
    for i, wins in enumerate(cardwins):
        if not wins:
            continue
        cards[i+1:i+wins+1] += cards[i]
    sol2 = sum(cards)
    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
