import random
import time


class ForestAdventure:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.choices = []
        self.encounters = {
            'mushroom': False,
            'tree': False,
            'help': False
        }
        self.jokes = [
            "Why don't trees use social media? Because they prefer logging in!",
            "What do you call a bear with no teeth? A gummy bear!",
            "Why did the mushroom go to the party? Because he was a fungi!",
            "What's a tree's favorite drink? Root beer!"
        ]
        self.riddles = [
            {"question": "What has roots as nobody sees, is taller than trees?", "answer": "mountain"},
            {"question": "I'm light as a feather, yet the strongest person can't hold me for long. What am I?",
             "answer": "breath"},
            {"question": "The more you take, the more you leave behind. What am I?", "answer": "footsteps"}
        ]

    def display_welcome(self):
        print("\n" + "=" * 50)
        print("🌲 Welcome to the Forest of Logic 🌲".center(50))
        print("=" * 50 + "\n")
        print("An interactive adventure where your choices shape your destiny!")
        print("Navigate through mysterious paths, solve puzzles, and discover secrets.\n")

    def get_player_info(self):
        self.name = input("Before we begin, what is your name, adventurer? ").strip()

        while True:
            try:
                self.age = int(input("How old are you? "))
                if 0 < self.age <= 120:
                    break
                print("Please enter a valid age between 1 and 120.")
            except ValueError:
                print("That doesn't look like a number. Try again!")

    def age_check(self):
        if self.age < 13:
            print(f"\nSorry {self.name}, you're too young for this adventure. Come back when you're older!")
            return False
        elif self.age < 18:
            print(f"\nTeen access granted, {self.name}. The forest whispers warnings as you enter...")
        else:
            print(f"\nAdult access granted, {self.name}. The ancient trees observe you carefully.")
        return True

    def main_menu(self):
        while True:
            print("\n" + "🌟 Main Menu 🌟".center(50, '~'))
            print("1. Start Adventure")
            print("2. Play the Number Guessing Game")
            print("3. Hear a Forest Joke")
            print("4. Exit")

            choice = input("\nChoose your path (1-4): ").strip()

            if choice == '1':
                self.start_adventure()
            elif choice == '2':
                self.guessing_game()
            elif choice == '3':
                self.tell_joke()
            elif choice == '4':
                print(f"\nFarewell, {self.name}. May the forest remember you kindly.")
                self.show_summary()
                break
            else:
                print("The forest doesn't understand your choice. Try again.")

    def start_adventure(self):
        self.choices.append("Started adventure")
        print("\nYou awaken in a misty forest. The air hums with ancient magic.")
        time.sleep(1)

        while True:
            print("\nBefore you lie three options:")

            # Dynamic options based on previous encounters
            options = []
            if not self.encounters['mushroom']:
                print("1. Follow the strange glowing path")
                options.append('1')
            if not self.encounters['tree']:
                print("2. Climb the towering ancient tree")
                options.append('2')
            if not self.encounters['help']:
                print("3. Call out for help")
                options.append('3')

            print("4. Return to main menu")
            options.append('4')

            path = input("What will you do? (" + "/".join(options) + "): ").strip()

            if path == '1' and '1' in options:
                self.follow_path()
            elif path == '2' and '2' in options:
                self.climb_tree()
            elif path == '3' and '3' in options:
                self.call_for_help()
            elif path == '4':
                print("You step back from the forest's edge...")
                break
            else:
                print("The forest echoes your confusion. Choose wisely.")

    def follow_path(self):
        self.encounters['mushroom'] = True
        self.choices.append("Followed the glowing path")
        print("\nAs you follow the glowing path, the air shimmers with magic.")
        time.sleep(1)
        print("A sentient mushroom blocks your way, its cap pulsing with light.")

        riddle = random.choice(self.riddles)
        print(f"\nThe mushroom asks: {riddle['question']}")
        answer = input("Your answer: ").lower()

        if riddle['answer'] in answer:
            print("\nThe mushroom glows brightly! 'Correct!' it chimes.")
            print("It gifts you a silver leaf that hums with power.")
            self.choices.append("Solved the mushroom's riddle")
        else:
            print("\nThe mushroom wilts slightly. 'Incorrect,' it sighs.")
            print("The path darkens as you continue your journey.")
            self.choices.append("Failed the mushroom's riddle")

    def climb_tree(self):
        self.encounters['tree'] = True
        self.choices.append("Climbed the ancient tree")
        print("\nYou scale the gnarled bark of the ancient tree.")
        time.sleep(1)

        if self.age < 18:
            print("From your high vantage point, you spot a safe path home!")
            print("The forest seems to guide you gently back to safety.")
            self.choices.append("Found safe path home")
        else:
            print("At the top, you see the forest edge... and shadowy figures watching you.")
            print("Your experience helps you recognize danger and retreat carefully.")
            self.choices.append("Spotted danger from tree")

    def call_for_help(self):
        self.encounters['help'] = True
        self.choices.append("Called for help")
        print("\nYour voice echoes through the trees.")
        time.sleep(1)

        helper = random.choice(['fox', 'raven'])
        if helper == 'fox':
            print("A friendly fox appears and leads you to safety!")
            self.choices.append("Rescued by fox")
        else:
            print("A raven lands nearby and whispers, 'Wrong move.'")
            print("The forest grows darker around you...")
            self.choices.append("Warned by raven")

    def guessing_game(self):
        self.choices.append("Played guessing game")
        print("\n🎲 Forest Number Guessing Game 🎲")
        print("Guess the magic number between 1-10. You have 3 attempts!")

        secret = random.randint(1, 10)
        attempts = 3
        won = False

        while attempts > 0 and not won:
            try:
                guess = int(input(f"\nAttempts left: {attempts}. Your guess: "))

                if guess == secret:
                    print("✨ The forest lights up! You guessed correctly!")
                    won = True
                    self.choices.append("Won guessing game")
                elif guess < secret:
                    print("The trees whisper: 'Higher...'")
                else:
                    print("The wind murmurs: 'Lower...'")

                attempts -= 1
            except ValueError:
                print("The forest only understands numbers here.")

        if not won:
            print(f"\nThe correct number was {secret}. Better luck next time!")
            self.choices.append("Lost guessing game")

    def tell_joke(self):
        joke = random.choice(self.jokes)
        print("\nThe forest spirits tell you a joke:")
        print(joke)
        self.choices.append("Heard a joke: " + joke[:20] + "...")

    def show_summary(self):
        if not self.choices:
            return

        print("\n" + "📜 Adventure Summary 📜".center(50, '~'))
        print(f"Adventurer: {self.name} (Age: {self.age})")
        print("\nYour journey included:")
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")
        print("\nUntil we meet again...\n")


def main():
    game = ForestAdventure()
    game.display_welcome()
    game.get_player_info()

    if game.age_check():
        game.main_menu()


if __name__ == "__main__":
    main()
