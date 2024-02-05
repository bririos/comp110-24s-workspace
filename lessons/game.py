"""Number Guessing game."""
from random import randint

SECRET: int =  randint(1,10)
#it wont change bc it is outside of loop
#while loop is false bc you want to enter while loop
correct: bool = False

while correct == False: #ese same thing as saying correct == False, not correct
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f"You got it right! {guess} is the secret number!")
        correct = True
    else:
        if SECRET < 5:
            print("Too High!")
        if SECRET > 10:
            print("Too low!")
        print("Try again!")





