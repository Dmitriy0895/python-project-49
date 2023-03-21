#!/usr/bin/env python3

import random
import brain_games.scripts.fb as fb


def brain_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    obj = {}
    for i in range(1, 4):
        question = random.randint(1, 99)
        if question % 2 == 0:
            answer = "yes"
        else:
            answer = 'no'
        obj[question] = answer
    return obj


def main():
    fb.games(brain_even)


if __name__ == '__main__':
    main()

