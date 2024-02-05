"""demostrate behavior of condtional"""

user_input: str = input("Pick a number: ")
print(type(user_input))
user_number: int = int(user_input)
print(type(user_number))


# if user number is less than 10, print "small"
if user_number % 2 ==0 :
    print("even")
else: # user_number >= 10
    print("odd")


print(user_number)


