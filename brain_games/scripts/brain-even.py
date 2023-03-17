#!/usr/bin/env python3

import prompt
import random


def main():
    ans = 'yes'

    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}")

    print("Answer 'yes' if the number is even, otherwise answer 'no'")
    for i in range(1, 4):
        num = random.randint(1, 99)
        print(f"Question: {num}")

        ans = "yes" if num % 2 == 0 else 'no'
        result = prompt.string('Your answer: ')

        if ans != result:
            print(f"{result} is wrong answer ;(. "
                  f"Correct answer was {ans}. "
                  f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
    return


if __name__ == '__main__':
    main()
