
import random
import time

levels = {
    "1": {
        "name": "Easy",
        "words": ["cat", "dog", "sun", "book", "terra"]
    },
    "2": {
        "name": "Medium",
        "words": ["python", "visual", "college", "studios", "games"]
    },
    "3": {
        "name": "Hard",
        "words": ["tanmay", "scramble", "knowledge",
                  "programming", "rishikesh"]
    }
}

print("===== WORD SCRAMBLE GAME =====")
time.sleep(1)

print("\nChoose your difficulty:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

level = input("\nEnter your choice (1/2/3): ")

if level not in levels:
    print("Invalid choice! Starting Easy mode.")
    level = "1"

selected = levels[level]
score = 0
rounds = 5

print(f"\nStarting {selected['name']} mode...")
time.sleep(1)

for round_num in range(1, rounds + 1):
    word = random.choice(selected["words"])

    # Scramble the word
    scrambled = word
    while scrambled == word:
        scrambled = ''.join(random.sample(word, len(word)))

    print(f"\nRound {round_num} of {rounds}")
    time.sleep(0.5)

    print("Unscramble this word:", scrambled)
    attempts = 3

    while attempts > 0:
        guess = input("Your guess (or 'quit'): ").lower().strip()

        if guess == "quit":
            print("\nLeaving the game...")
            time.sleep(1)
            break

        if guess == word:
            print("Correct! +1 point!")
            score += 1
            break
        else:
            attempts -= 1

            if attempts > 0:
                print(f"Wrong! Try again. Attempts left: {attempts}")
            else:
                print("Out of attempts!")
                print("The correct word was:", word)

        time.sleep(0.5)

    if guess == "quit":
        break

    time.sleep(1)
    print("-" * 30)

print("\nCalculating your final score...")
time.sleep(1)

print("\n===== GAME OVER =====")
print("Difficulty:", selected["name"])
print("Final score:", score, "/", rounds)

if score == rounds:
    print("Perfect score! Amazing!")
elif score >= 3:
    print("Great job!")
else:
    print("Keep practicing!")

time.sleep(1)
print("Thanks for playing!")
