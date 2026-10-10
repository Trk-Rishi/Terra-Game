import time
import random


def select_mode():
    print("Select a mode:")
    print("Press 1 for Higher/Lower Mode")
    print("Press 2 for Hot/Cold Mode")
    m = int(input())
    print()
    return m

def select_difficulty():
    print("Select your difficulty: ")
    print("Press 1 for Easy (1-100)")
    print("Press 2 for Medium (1-1000)")
    print("Press 3 for Hard (1-10000)")
    d = int(input())
    print()
    if d == 1:
        return 100
    elif d == 3:
        return 10000
    elif d == 2:
        return 1000
    else:
        return d
def guessing_highlow(r):
    answer = random.randint(1,r)
    num_guesses = 0
    guess = int(input("Enter your guess: "))
    while True:
        
        if answer > guess:
            print("Guess Higher!!")
            guess = int(input("Enter your guess: "))
            num_guesses += 1
            
        elif guess > answer:
            print("Guess Lower!!")
            guess = int(input("Enter your guess: "))
            num_guesses += 1
        elif guess == answer:
            num_guesses += 1
            return num_guesses
            break        






        
def guessing_hotcold(r):
    answer = random.randint(1,r)
    num_guesses = 0
    guess = int(input("Enter your guess: "))
    difference = abs(answer - guess)
    while True:
        difference = abs(answer - guess)
        if r == 100:  #easy
            if difference > 45:
                print("Very Cold !!!") 
                guess = int(input("Enter your guess: "))
                num_guesses += 1
            elif difference > 35:
                print("Cold !!!")
                guess = int(input("Enter your guess: "))
                num_guesses += 1
            
            elif difference > 25:
                print("Warm !!!")
                guess = int(input("Enter your guess: "))
                num_guesses += 1
            elif difference > 15:
                print("Warmmer !!!")
                guess = int(input("Enter your guess: "))
                if guess < answer:
                    print("Hint: Guess higher.")
                elif guess > answer:
                    print("Hint: Guess lower.")
                num_guesses += 1
            elif difference > 0:
                print("Hot !!!")
                guess = int(input("Enter your guess: "))
                num_guesses += 1
                if guess < answer:
                    print("Hint: Guess higher.")
                elif guess > answer:
                    print("Hint: Guess lower.")
            elif difference == 0:
                num_guesses += 1
                return num_guesses
                break
        if r == 1000:  #medium (1-1000)
            if difference > 350:
                print("Very Cold !!!") 
                guess = int(input("Enter your guess: "))
                num_guesses += 1
            
            elif difference > 200:
                print("Cold !!!")
                guess = int(input("Enter your guess: "))
                num_guesses += 1
            
            elif difference > 120:
                print("Warm !!!")
                guess = int(input("Enter your guess: "))
                num_guesses += 1
            elif difference > 50:
                print("Hot !!!")
                guess = int(input("Enter your guess: "))
                num_guesses += 1
                if guess < answer:
                    print("Hint: Guess higher.")
                elif guess > answer:
                    print("Hint: Guess lower.")
            elif difference > 0:
                print("Very Hot !!!")
                guess = int(input("Enter your guess: "))
                num_guesses += 1
                if guess < answer:
                    print("Hint: Guess higher.")
                elif guess > answer:
                    print("Hint: Guess lower.")
            elif difference == 0:
                num_guesses += 1
                return num_guesses
                break
        if r == 10000:  #hard (1-10000)
            if difference > 2000:
                print("Very Cold !!!") 
                guess = int(input("Enter your guess: "))
                num_guesses += 1
            
            elif difference > 750:
                print("Cold !!!")
                guess = int(input("Enter your guess: "))
                num_guesses += 1
            
            elif difference > 500:
                print("Warm !!!")
                guess = int(input("Enter your guess: "))
                num_guesses += 1
            elif difference > 250:
                print("Hot !!!")
                guess = int(input("Enter your guess: "))
                num_guesses += 1
                if guess < answer:
                    print("Hint: Guess higher.")
                elif guess > answer:
                    print("Hint: Guess lower.")
            elif difference > 100:
                print("Very Hot !!!")
                guess = int(input("Enter your guess: "))
                num_guesses += 1
                if guess < answer:
                    print("Hint: Guess higher.")
                elif guess > answer:
                    print("Hint: Guess lower.")
            elif difference > 10:
                print("Super Hot !!!")
                guess = int(input("Enter your guess: "))
                if guess < answer:
                    print("Hint: Guess higher.")
                elif guess > answer:
                    print("Hint: Guess lower.")
            elif difference > 0:
                print("ALMOST THERE !!!")
                guess = int(input("Enter your guess: "))
                if guess < answer:
                    print("Hint: Guess higher.")
                elif guess > answer:
                    print("Hint: Guess lower.")
                num_guesses += 1
            elif difference == 0:
                num_guesses += 1
                return num_guesses
                break
        
def play_again():
    print("Press 1 to play again.")
    print("Press anything else to exit")
    k = int(input())
    if k == 1:
        return True
    else:
        return False
best_score = 0
game_number = 1
def game_start():
    global best_score
    global game_number
    print()
    print("Game is starting now...")
    print("This is game number:",game_number)
    time.sleep(1.5)
    print()
    

    difficulty = select_difficulty()
    time.sleep(1.5)
    while True:
        if difficulty < 100 or (difficulty > 100 and difficulty < 1000) or (difficulty < 10000 and difficulty > 1000) and difficulty > 10000:
            print("Choose a valid difficulty.")
            time.sleep(1)
            difficulty = select_difficulty()
        else:
            break

    mode = select_mode()
    time.sleep(1.5)
    while mode > 2 or mode < 1:
        print("Choose a valid mode.")
        time.sleep(1)
        mode = select_mode()
    if mode == 1:
        time.sleep(1.5)
        score = guessing_highlow(difficulty)
        time.sleep(1.5)
        if game_number == 1:
            best_score = score
        print()
        print("Congratulations!!! You Guesssed Correctly")
        print("Your Score is:",score)
        print("Your best score is: ",best_score)
        print()
        time.sleep(1)
        game_number += 1
        if score < best_score:
            best_score = score
        if play_again():
            time.sleep(1)
            game_start()
    elif mode == 2:
        time.sleep(1.5)
        score = guessing_hotcold(difficulty)
        time.sleep(1.5)
        if game_number == 1:
            best_score = score
        print()
        print("Congratulations!!! You Guesssed Correctly")
        print("Your Score is:",score)
        game_number += 1
        print("Your best score is: ",best_score)
        print()
        time.sleep(1)
        if score < best_score:
            best_score = score
        if play_again():
            time.sleep(1)
            game_start()

game_start()