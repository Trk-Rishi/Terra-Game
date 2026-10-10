import time
import random


def select_mode():
    print("Select a mode:")
    print("Press 1 for Higher/Lower Mode")
    print("Press 2 for Hot/Cold Mode")
    m = int(input("1 or 2"))
    return m

def select_difficulty():
    print("Select your difficulty: ")
    print("Press 1 for Easy (1-100)")
    print("Press 2 for Medium (1-1000)")
    print("Press 3 for Hard (1-10000)")
    d = int(input("1 or 2 or 3"))
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
            elif difference > 10:
                print("Hot !!!")
                guess = int(input("Enter your guess: "))
                num_guesses += 1
                if guess < answer:
                    print("Hint: Guess higher.")
                elif guess > answer:
                    print("Hint: Guess lower.")
            elif difference == 0:
                print("yaya")
                print("Number of guesses :",num_guesses)
                num_guesses += 1
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
            elif difference > 15:
                print("Very Hot !!!")
                guess = int(input("Enter your guess: "))
                num_guesses += 1
                if guess < answer:
                    print("Hint: Guess higher.")
                elif guess > answer:
                    print("Hint: Guess lower.")
            elif difference == 0:
                print("yaya")
                print("Number of guesses :",num_guesses)
                num_guesses += 1
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
                num_guesses += 1
            elif difference == 0:
                print("yaya")
                print("Number of guesses :",num_guesses)
                num_guesses += 1
                break
        

                
        
def game_start():
    mode = select_mode()
    if mode == 1:
        pass


guessing_hotcold(1000)


