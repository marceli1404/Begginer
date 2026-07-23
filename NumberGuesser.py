import random
import sys

# NumberGuesser.py
# Simple interactive number guessing game.
# Modes: user guesses computer's number OR computer guesses user's number.


def input_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            s = input(prompt).strip()
            v = int(s)
            if (min_val is not None and v < min_val) or (max_val is not None and v > max_val):
                print(f"Enter a number between {min_val} and {max_val}.")
                continue
            return v
        except ValueError:
            print("Please enter an integer.")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            sys.exit(0)

def yes_no(prompt):
    while True:
        try:
            r = input(prompt).strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            sys.exit(0)
        if r in ("y","yes"):
            return True
        if r in ("n","no"):
            return False
        print("Please answer y/n.")

def user_guesses(low, high):
    target = random.randint(low, high)
    attempts = 0
    print(f"Guess the number between {low} and {high}.")
    while True:
        guess = input_int("Your guess: ", low, high)
        attempts += 1
        if guess == target:
            print(f"Correct! Attempts: {attempts}")
            return attempts
        if guess < target:
            print("Higher.")
        else:
            print("Lower.")

def computer_guesses(low, high):
    print(f"Think of a number between {low} and {high}. I will try to guess it.")
    input("Press Enter when ready...")
    attempts = 0
    lo, hi = low, high
    while lo <= hi:
        attempts += 1
        guess = (lo + hi) // 2
        while True:
            try:
                resp = input(f"My guess is {guess}. Is it (h)igher, (l)ower, or (c)orrect? ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\nExiting.")
                sys.exit(0)
            if resp in ("h","higher"):
                lo = guess + 1
                break
            if resp in ("l","lower"):
                hi = guess - 1
                break
            if resp in ("c","correct"):
                print(f"I got it in {attempts} attempts.")
                return attempts
            print("Please answer with 'h', 'l', or 'c'.")
        if lo > hi:
            print("Inconsistent answers detected. Are you sure? Let's stop.")
            return attempts

def choose_range():
    print("Choose range for the game.")
    low = input_int("Low (default 1): ") if yes_no("Use custom range? (y/n): ") else 1
    if low is None:
        low = 1
    high = input_int("High: ", min_val=low)
    return low, high

def main():
    print("Number Guesser")
    while True:
        print("\nModes:\n1) You guess the computer's number\n2) Computer guesses your number\n3) Quit")
        choice = input("Choose 1/2/3: ").strip()
        if choice == "3":
            print("Goodbye.")
            break
        if choice not in ("1","2"):
            print("Invalid choice.")
            continue
        if choice == "1":
            if yes_no("Custom range? (y/n): "):
                low = input_int("Low: ")
                high = input_int("High: ", min_val=low)
            else:
                low, high = 1, 100
            user_guesses(low, high)
        else:
            if yes_no("Custom range? (y/n): "):
                low = input_int("Low: ")
                high = input_int("High: ", min_val=low)
            else:
                low, high = 1, 100
            computer_guesses(low, high)

if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nExiting.")
        sys.exit(0)