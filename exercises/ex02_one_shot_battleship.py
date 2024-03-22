"""EX02 - One Shot Battleship - A cute step toward Battles."""
__author__ = "730576067"
grid_size: int = 4
secret_guess_row: int = 3
secret_guess_column: int = 2

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

guess_row: int = int(input("Guess a row: "))
while guess_row > grid_size or guess_row < 1:
    guess_row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
guess_column: int = int(input("Guess a column: "))
while guess_column > grid_size or guess_column < 1:
    guess_column = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

result: str = ""
if guess_row == secret_guess_row and guess_column == secret_guess_column:
    result += RED_BOX
else:
    result += WHITE_BOX
counter_row: int = 1 

while counter_row <= grid_size:
    emoji_string_row: str = ""
    counter_column: int = 1 
    if guess_row == counter_row:
        while counter_column <= grid_size:
            if guess_column == counter_column:
                emoji_string_row += result 
            else:
                emoji_string_row += BLUE_BOX
            counter_column += 1
    else:
        while counter_column <= grid_size:
            emoji_string_row += BLUE_BOX
            counter_column += 1
    print(emoji_string_row)
    counter_row += 1
if guess_row == secret_guess_row and guess_column == secret_guess_column:
    print("Hit!")
elif guess_column != secret_guess_column and guess_row == secret_guess_row:
    print("Close! Correct row, wrong column.")
elif guess_column == secret_guess_column and guess_row != secret_guess_row:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")
