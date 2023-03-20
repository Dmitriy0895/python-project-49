#!/usr/bin/env python3

import prompt
import random


def games(game='brain_even'):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}")

    number1, number2, arithm, question, answer = 0, 0, '', '', 0

    message = {
        'brain_even': "Answer 'yes' if the number is even, otherwise answer 'no'",
        'brain_calc': "What is the result of the expression?"
    }

    print(message[game])

    for i in range(1, 4):

        if game == 'brain_even':
            question = random.randint(1, 99)
            if question % 2 == 0:
                answer = "yes"
            else:
                answer = 'no'
        elif game == 'brain_calc':

            arithmetic = {
                "+": lambda x, y: x + y,
                "-": lambda x, y: x - y,
                "*": lambda x, y: x * y,
            }
            number1 = random.choice(range(1, 11))
            number2 = random.choice(range(1, 11))
            arithm = random.choice(list(arithmetic.keys()))
            question = str(number1) + str(arithm) + str(number2)
            answer = str(arithmetic[arithm](number1, number2))

        print(f"Question: {question}")

        result = prompt.string('Your answer: ')

        if answer != result:
            print(f"{result} is wrong answer ;(. "
                  f"Correct answer was {answer}. "
                  f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")
    return
