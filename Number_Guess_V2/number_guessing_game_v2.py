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
    
def guessing(r):
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
        
def game_start():
    mode = select_mode()
    if mode == 1:
        pass

x = guessing(100)

