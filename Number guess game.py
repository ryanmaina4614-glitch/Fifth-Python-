import random
import os
import json

HS_FILE = "highscore.txt"
LEADERBOARD_FILE = "leaderboard.json"


def load_high_score():
    """Return the best (lowest) score stored in HS_FILE or None if unavailable."""
    try:
        with open(HS_FILE) as f:
            return int(f.read().strip())
    except Exception:
        return None


def save_high_score(score):
    with open(HS_FILE, "w") as f:
        f.write(str(score))


def load_leaderboard():
    """Return list of {'name':str,'score':int} sorted by score."""
    try:
        with open(LEADERBOARD_FILE) as f:
            data = json.load(f)
            return sorted(data, key=lambda x: x["score"])
    except Exception:
        return []


def save_leaderboard(lb):
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(lb, f, indent=2)


def display_leaderboard(lb):
    if not lb:
        print("(no entries yet)")
        return
    print("🏅 Leaderboard (best scores)")
    for idx, entry in enumerate(lb, start=1):
        print(f" {idx}. {entry['name']} - {entry['score']} attempts")


def number_guessing_game():
    print("🎮 Welcome to the Number Guessing Game!")
    player = input("What's your name? ").strip() or "Anonymous"
    print(f"Hello, {player}!")
    print("I am thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0

    leaderboard = load_leaderboard()
    display_leaderboard(leaderboard)
    high_score = load_high_score()
    if high_score is not None:
        print(f"🏆 Current high score: {high_score} attempts")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("⚠️ Please enter a number between 1 and 100.")
                continue

            if guess < secret_number:
                print("📉 Too low! Try again.")
            elif guess > secret_number:
                print("📈 Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
                if high_score is None or attempts < high_score:
                    print("💾 That's a new high score!")
                    save_high_score(attempts)
                leaderboard.append({"name": player, "score": attempts})
                leaderboard = sorted(leaderboard, key=lambda x: x["score"])[:10]
                save_leaderboard(leaderboard)
                print()
                display_leaderboard(leaderboard)
                break

        except ValueError:
            print("❌ Please enter a valid number.")


def main():
    while True:
        number_guessing_game()
        again = input("Play again? (y/N): ").strip().lower()
        if again != "y":
            print("Thanks for playing – goodbye!")
            break

if __name__ == "__main__":
    main()