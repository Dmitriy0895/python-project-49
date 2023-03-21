#!/usr/bin/env python3

import random
import brain_games.scripts.fb as fb


def brain_gcd():
    obj = {}
    print("Find the greatest common divisor of given numbers")
    for i in range(1, 4):
        a = random.choice(range(1, 99))
        b = random.choice(range(1, 99))
        question = f"{a} {b}"
        if a < b:
            a, b = b, a

        while b:
            a, b = b, a % b

        answer = str(a)

        obj[question] = answer
    return obj


def main():
    fb.games(brain_gcd)


if __name__ == '__main__':
    main()
