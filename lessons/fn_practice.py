"""Example functions to learn definitios and calling syntax"""


def my_max(num1: int, num2:int)-> int:
    """Rturns the max value out of two numbers"""
    if num1 >= num2:
        return num1
    else: #num1<num 2
        return num2
max_num: int =my_max(1,10)
#they have to be the same type
other_max: int =my_max(11,3)
#define function before calling

print(max_num)
print(other_max)

    