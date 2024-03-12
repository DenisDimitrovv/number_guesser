import random

guess = int(input("Put a number between 1 and 10: "))
number = random.randrange(0, 10)

while number != guess:

    if guess < number:
        print("Try upper")
        guess = int(input("Enter a number again: "))

    elif guess > number:
        print("Try lower")
        guess = int(input("Enter a number again: "))
    else:
        break
print("You won")
