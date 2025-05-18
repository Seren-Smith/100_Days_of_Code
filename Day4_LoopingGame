import random

def skip_count_printer():
    """Skip-count printer that skips multiples of 4"""
    print("\nSkip-Count Printer")
    try:
        n = int(input("Enter a number: "))
        for i in range(1, n + 1):
            if i % 4 == 0:
                continue
            print(i)
    except ValueError:
        print("Please enter a valid number.")


def word_analyzer():
    """Analyzes each character in a word/sentence"""
    print("\nWord Analyzer")
    word = input("Enter a word or sentence: ")
    vowels = {'a', 'e', 'i', 'o', 'u'}
    for index, char in enumerate(word):
        lower_char = char.lower()
        vowel_status = "Vowel!" if lower_char in vowels else "Not a vowel"
        print(f"Index {index}: {char} - {vowel_status}")


def repeating_reminder():
    """Repeating reminder that stops when user types 'stop'"""
    print("\nRepeating Reminder")
    print("Type 'stop' to end this reminder.")
    while True:
        print("💧 Drink water!")
        user_input = input("> ").lower()
        if user_input == "stop":
            break


def guessing_game():
    """Unlimited guessing game with random secret number"""
    print("\n🎮 Guessing Game 🎮")
    secret_number = random.randint(1, 20)
    attempts = 0

    print("Guess a number between 1 and 20 (type 'exit' to quit):")
    while True:
        guess = input("Your guess: ")

        if guess.lower() == 'exit':
            print(f"Game ended. The secret number was {secret_number}.")
            break

        try:
            guess_num = int(guess)
            attempts += 1
        except ValueError:
            print("Please enter a valid number or 'exit'.")
            continue

        if guess_num < secret_number:
            print("Too low! Try again.")
        elif guess_num > secret_number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts!")
            break


def main():
    """Main menu for the Loop Lab Machine"""
    print("\nWelcome to Loop Lab")

    while True:
        print("\nChoose a module:")
        print("1. Skip-Count Printer")
        print("2. Word Analyzer")
        print("3. Repeating Reminder")
        print("4. Guessing Game")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            skip_count_printer()
        elif choice == '2':
            word_analyzer()
        elif choice == '3':
            repeating_reminder()
        elif choice == '4':
            guessing_game()
        elif choice == '5':
            print("👋 Thanks for using Loop Lab! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
