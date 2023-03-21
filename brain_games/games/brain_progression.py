#!/usr/bin/env python3

import random
import brain_games.scripts.fb as fb


def brain_progression():
    obj = {}
    print("What number is missing in the progression?")
    for i in range(1, 4):
        arr, n = [], 0
        a = random.randint(1, 50)
        b = random.randint(1, 5)
        c = random.randint(0, 9)
        while n <= 10:
            a += b
            arr.append(a)
            n += 1
        res = arr.pop(c)
        arr.insert(c, '..')
        question = " ".join(map(str, arr))
        answer = str(res)

        obj[question] = answer
    return obj


def main():
    fb.games(brain_progression)


if __name__ == '__main__':
    main()
