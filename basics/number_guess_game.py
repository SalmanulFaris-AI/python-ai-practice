import random

secret = random.randint(1, 10)

print("Guess a number between 1 and 10")
print("you have 3 chances")

for i in range(3):
    guess = int(input("Enter your guess: "))

    if guess == secret:
        print("Correct! 🎉")
        break
    else:
        print("Wrong 😅 try again")
else:
    print("game over number was",secret)
