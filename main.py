
import random


def play_game():
    """Run the number guessing game."""

    secret_number = random.randint(1, 100)
    attempts = 0

    print("\n" + "=" * 40)
    print("       NUMBER GUESSING GAME")
    print("=" * 40)
    print("I have selected a number between 1 and 100.")
    print("Try to guess the correct number!")
    print("=" * 40)

    while True:
        try:
            guess = int(input("\nEnter your guess (1-100): "))

        except ValueError:
            print("Invalid input! Please enter a valid integer.")
            continue

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try a higher number.")

        elif guess > secret_number:
            print("Too high! Try a lower number.")

        else:
            print("\n" + "=" * 40)
            print("       CONGRATULATIONS!")
            print("=" * 40)
            print(f"Correct number: {secret_number}")
            print(f"Total attempts: {attempts}")

            if attempts == 1:
                print("Amazing! You guessed it on your first try!")
            elif attempts <= 5:
                print("Excellent! You guessed it in very few attempts.")
            elif attempts <= 10:
                print("Great job! You found the correct number.")
            else:
                print("Well played! Keep practicing.")

            print("=" * 40)
            break


def main():
    """Start the number guessing game."""

    while True:
        play_game()

        play_again = input(
            "\nWould you like to play again? (yes/no): "
        ).strip().lower()

        if play_again not in ("yes", "y"):
            print("\nThank you for playing!")
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
