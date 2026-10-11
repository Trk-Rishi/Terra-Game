import random
import time

choices = {
    "rock": "(ง'̀-'́)ง   [ROCK]",
    "paper": "( ^_^)/   [PAPER]",
    "scissors": "✂ (^-^) ✂    [SCISSORS]",
    "Rock": "(ง'̀-'́)ง   [ROCK]",
    "Paper": "( ^_^)/   [PAPER]",
    "Scissors": "✂ (^-^) ✂    [SCISSORS]"
}

current_streak = 0
highest_streak = 0

print("================================")
print("   ROCK PAPER SCISSORS GAME")
print("================================")

time.sleep(1)
print("Choose your weapon!!!")
time.sleep(0.5)
print("Rock | Paper | Scissors ")
print("Type 'Exit' to exit.\n")

def call_user():
    print("This Program was written by Tanmay Rishikesh")
    return "Svg"

while True:
    player = input("Your choice: ").lower().strip()

    if player == "Exit" or player == "exit":
        print("\n================================")
        print("          GAME OVER")
        print("================================")
        print(f"Highest winning streak: {highest_streak}")
        print("Thanks for playing! (^-^)/")
        break

    if player not in choices:
        print("Invalid choice!! Try again!! (o_O)\n")
        continue

    print("\nYou selected:")
    time.sleep(1)
    print(choices[player])

    time.sleep(1)
    print("\nComputer is choosing", end="", flush=True)

    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)

    computer = random.choice(list(choices.keys()))

    print("\n\nComputer selected:")
    time.sleep(1)
    print(choices[computer])

    time.sleep(0.5)

    if player == computer:
        print("\nIt's a tie! (¬_¬)")
        current_streak = 0

    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print("\nYou WIN! \\(^o^)/")
        current_streak += 1

        if current_streak > highest_streak:
            highest_streak = current_streak
            print("NEW HIGHEST STREAK!!!")

    else:
        print("\nYou LOSE! (T_T)")
        current_streak = 0

    print(f"\nCurrent winning streak: {current_streak}")
    print(f"Highest winning streak: {highest_streak}")
    print("\n" + "-" * 32 + "\n")
    time.sleep(1)
