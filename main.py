import random

import art

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess, answer):
    if guess > answer:
        print("Too high")
        print("Guess again.")
    elif guess < answer:
        print("Too low")
        print("Guess again.")
    else:
        print(f"You got it! The answer is {answer}")
        return True


def set_difficulty():
    easy_or_hard = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if easy_or_hard == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


print(art.logo)
answer = random.randint(1, 100)

life = set_difficulty()
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while life > 0:
    print(f"You have {life} attempts remaining to guess the number.")
    life -= 1
    guess = int(input("Make a guess: "))
    if check_answer(guess, answer):
        break
    elif life == 0:
        print("You've run out of guesses, You lose.")