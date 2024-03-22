"""battleship function."""
__author__ = "730576067"

import random


def input_guess(size_grid: int, row_column: str) -> int: 
    """Inputs a guess."""
    assert row_column == "row" or row_column == "column"
    if guess == "row":
        guess = input("Guess a row: ")
    elif guess == "column":
        guess = input("Guess a column: ")
    while size_grid < guess:
        guess = int(input(f"The grid is only {size_grid} by {size_grid}. Try again: "))
    else:
        return guess


BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def print_grid(size_grid: int, row_guess: int, column_guess: int, correct: bool) -> None:
    """Prints grid."""
    result: str = ""
    if correct is True:
        result += RED_BOX
    else:
        result += WHITE_BOX
    counter_row: int = 1
    while counter_row <= size_grid:
        emoji_string_row: str = ""  
        counter_column: int = 1 
        while counter_column <= size_grid:
            if column_guess == counter_column and row_guess == counter_row:
                emoji_string_row += result 
            else:
                emoji_string_row += BLUE_BOX
            counter_column += 1
        counter_row += 1
        print(emoji_string_row)
    return (None)

def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """False or True guess."""
    if secret_row == row_guess and secret_column == column_guess:
        return True     
    elif secret_row or secret_column != row_guess or column_guess:  
        return False


def main(grid_size: int, secret_row: int, secret_column: int) -> None:  
    """Puts together all functions."""
    turns: int = 1
    won: bool = True
    while turns <= 5 and won is True:
        print(f"===Turn {turns}/5 ===")
    row: int = input_guess(grid_size, "row")
    column: int = input_guess(grid_size, "column")
    guess: bool = correct_guess(secret_row, secret_column, row, column)
    print_grid(grid_size, row, column, guess)
    if guess is True:
        print("Hit!")
        print(f"You won {turns}/5 turns!")
        won = False
    else:
        print("Miss!")
        turns += 1
    if won is False:
        print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))