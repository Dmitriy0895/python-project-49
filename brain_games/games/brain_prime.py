#!/usr/bin/env python3

import random
import brain_games.scripts.fb as fb


def brain_prime():
    obj = {}
    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")
    for i in range(1, 4):
        question = random.randint(2, 100)
        for j in range(2, question):
            if question % j == 0:
                answer = 'no'
                break
            else:
                answer = 'yes'

        obj[question] = answer
    return obj


def main():
    fb.games(brain_prime)


if __name__ == '__main__':
    main()