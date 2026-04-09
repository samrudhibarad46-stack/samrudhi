import random

try:
    number = random.randint(1, 10)
    guess = int(input("Guess a number (1-10): "))

    if guess == number:
        print("Correct! 🎉")
    else:
        print("Wrong! The number was", number)

except ValueError:
    print("Please enter a valid number!")

finally:
    print("Game over.")