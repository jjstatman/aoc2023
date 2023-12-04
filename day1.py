import numpy as np

if __name__ == "__main__":
    sol1 = 0
    sol2 = 0
    with open("day1.txt") as f:
        for line in f.read().split('\n'):
            for letter in line:
                if letter.isdigit():
                    sol1 += 10*int(letter)
                    break
            for letter in line[::-1]:
                if letter.isdigit():
                    sol1 += int(letter)
                    break
            line = line.replace("one","o1e").replace("two","t2o").replace("three","t3e").replace("four","f4r").replace("five","f5e").replace("six","s6x").replace("seven","s7n").replace("eight","e8t").replace("nine","n9e")
            for letter in line:
                if letter.isdigit():
                    sol2 += 10*int(letter)
                    break
            for letter in line[::-1]:
                if letter.isdigit():
                    sol2 += int(letter)
                    break
    print('Solution 1:', sol1)
    print('Solution 2:', sol2)
