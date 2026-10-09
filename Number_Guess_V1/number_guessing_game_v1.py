### NUMBER GUESSING GAME
### HIGHER OR LOWER
### NUMBER BETWEEN 1-1000

##Libraries needed
import random
import time

"""
LOGIC :
first we get a random number 
which will be our answer

we take input from user
if its lower or higher , we show that

and take input again until he guesses it right

we display his score
"""


###Time is so we can add a little pause between guesses and outputs 
num_guesses = 0 #initialize score
answer = random.randint(1,1000)
print("Guess the Random Number !!")
print("..........")
time.sleep(1)
guess = int(input("Enter your guess: "))
print("..........")
time.sleep(1)
while True:
    if answer > guess:
        print("Guess Higher!!")
        guess = int(input("Enter your guess: "))
        num_guesses += 1
        print("..........")
        time.sleep(1)
    elif guess > answer:
        print("Guess Lower!!")
        guess = int(input("Enter your guess: "))
        num_guesses += 1
        print("..........")
        time.sleep(1)

    elif guess == answer:
        num_guesses += 1
        print("Congratulations , You guess correctly")
        print("..........")
        time.sleep(1)
        print("The number was :",answer)
        print("..........")
        time.sleep(1)
        print("Total Number of Attempts: ",num_guesses)
        print("..........")
        print()
        break        
#Therefore this is finally done and we can run this code to play the game and guess the number between 1-1000