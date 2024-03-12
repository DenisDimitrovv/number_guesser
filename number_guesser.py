import random

guesses = 1
guess = int(input("Put a number between 1 and 10: "))
number = random.randrange(0, 10)

while number != guess:
    guesses += 1
    if guess < number:
        print("Try upper")
        guess = int(input("Enter a number again: "))
    elif guess > number:
        print("Try lower")
        guess = int(input("Enter a number again: "))
    else:
        break
print(f"You won with {guesses} guesses.")