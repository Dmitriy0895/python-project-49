#!/usr/bin/env python3

import prompt
import random


def games(fn):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}")

    obj = fn()

    for key, val in obj.items():
        print(f"Question: {key}")

        result = prompt.string('Your answer: ')

        if val != result:
            print(f"{result} is wrong answer ;(. "
                  f"Correct answer was {val}. "
                  f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
    return

