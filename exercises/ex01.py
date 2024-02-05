"""EX01 - Simple Battleship - A cute step toward Battles"""

__author__ = "730576067"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

empty_string: str= ""
empty_emoji: str = ""

guess_secret: str = input("Pick a secret boat location between 1 and 4: ")

   
if int(guess_secret) > 4:
    print(f"Error! {guess_secret} too high!")
    exit()
if int(guess_secret) < 1:
    print(f"Error! {guess_secret} too low!")
    exit()
person2_guess: str = input("Guess a number between 1 and 4: ") 

if int(person2_guess) > 4:
    print(f"Error! {person2_guess} too high!")
    exit()
if int(person2_guess) < 1:
    print(f"Error! {person2_guess} too low!")
    exit()

if int(person2_guess) == int(guess_secret):
    print("Correct! You hit the ship.")
    empty_emoji+= RED_BOX
else: 
    print("Incorrect! You missed the ship.")
    empty_emoji += WHITE_BOX
   


if int(person2_guess) == 1:
    empty_string += empty_emoji
else:
    empty_string = empty_string + BLUE_BOX

if int(person2_guess) == 2:
    empty_string += empty_emoji
else: 
    empty_string = empty_string + BLUE_BOX

if int(person2_guess) == 3:
    empty_string += empty_emoji
else: 
    empty_string = empty_string + BLUE_BOX

if int(person2_guess) == 4:
    empty_string += empty_emoji
else: 
    empty_string = empty_string + BLUE_BOX
   
print(empty_string)





