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


"""
Ideas for V2 --->
Hot/Cold Option
Tracks Best Score (function for new guess added)
"""
###Time is so we can add a little pause between guesses and outputs 

answer = random.randint(1,1000)
print("Hi")
print(answer)
guess = int(input("Enter your guess: "))

while True:
    if answer > guess:
        print("Guess Higher!!")
        guess = int(input("Enter your guess: "))
        
    elif guess > answer:
        print("Guess Lower!!")
        guess = int(input("Enter your guess: "))

    elif guess == answer:
        print("Congratulations , You guess correctly")
        break        
