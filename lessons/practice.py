age: int = int(input("What is your age?"))
if age <= 12:
    price = 5
else:
    price: int = 10

print(price)

age: int = int(input("What is your age?"))
if age <= 12:
    price: int = 5
elif age > 60:
    price: int = 5
else:
    price: int = 10
print(price)

age: int = int(input("What is your age?"))
if (age <= 12) or (age > 60):
    price: int = 5
else:
    price: int = 10
print(price)

age: int = int(input("What is your age?"))
if age <= 12:
    price: int = 5
elif age <= 60:
    price: int = 10
print(price)  