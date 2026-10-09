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

Answer = random.randint(1,1000)
Guess = int(input("Enter your guess: "))
while Guess != Answer:
    print("working")