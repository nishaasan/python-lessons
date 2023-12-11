import random

def guess_the_number():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            # Get the player's guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
