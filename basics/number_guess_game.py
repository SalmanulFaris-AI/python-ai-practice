import random

secret = random.randint(1, 10)

print("Guess a number between 1 and 10")

guess = int(input("Enter your guess: "))

if guess == secret:
    print("Correct! 🎉")
else:
    print("Wrong 😅 The number was:", secret)
