""" Practice while loops and debug them."""

my_number: int =8675309
my_number_str: str = str(my_number)
index:int=0
total: int =0


while index < len(my_number_str):
    index+= 1
    value: int = int (my_number_str[index])
    total+=value
    