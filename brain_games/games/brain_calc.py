#!/usr/bin/env python3

import random
import brain_games.scripts.fb as fb


def brain_calc():
    print("What is the result of the expression?")
    obj = {}
    for i in range(1, 4):
        arithmetic = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
        }
        number1 = random.choice(range(1, 11))
        number2 = random.choice(range(1, 11))
        arithm = random.choice(list(arithmetic.keys()))
        question = f"{number1} {arithm} {number2}"
        answer = str(arithmetic[arithm](number1, number2))
        obj[question] = answer
    return obj


def main():
    fb.games(brain_calc)


if __name__ == '__main__':
    main()
