# Terra-Games


## Number Guessing V1
What we need :
first we get a random number 
which will be our answer

we take input from user
if its lower or higher , we show that

and take input again until he guesses it right

we display his score

LOGIC : 

we generate a random number using 
RANDOM Module
we use a specific range of 1-1000


we need input again and again until the guess is CORRECT 
so we use WHILE loop for that


CORRECT as in == to the random number we generate
so we use simple comparision operators

if the guess is higher than the number 
 then we say to guess higher and get the input again

if the guess is lower than the number
then we say to guess lower and get the input again


if the guess is correct
we say that guess is correct and display the score

score is a global variable 
that is initialised at 0 and incremeneted by 1 at every guess




Ideas for V2 --->
Hot/Cold Option
Add try again feature (Recursion)
Tracks Best Score (function for new guess added)
Set Range

## Number Guessing V2:

### Prepared Ideas :

Hot/Cold Option and Higher/Lower option
Add try again feature (Recursion)
Tracks Best Score (function for new guess added)
Set Range


### WILL DEFINE DIFFERENT FUNCTIONS FOR ALL OF THEM

SelectMode --->  Selects whether hot/cold or highr/lower mode
SelectDifficulty ---> Selects difficulty level
PlayAgain ---> Starts a new game
GuessingHighLow ----> Starts game on mode higher/lower
GuessingHotCold ----> Starts game on mode hot/cold
GameStart ----> Executes and calls all games and keeps score


## HANGMAN

Word Guessing Game :
random words are given

one of them is selected 

we get 6 guesses
one letter at a time

6 stages of hangman are shown.

### How code works
Words are stored in a list
stages of hangman are stored in a list
time.sleep is used between outputs
random module is used to select a random word from the list
While Loop is used to iterate through all guesses
"_" is shown for every unguessed letter
strip and lower are used when taking input from user incase they press "Space" or a capital letter
if more letters or a non-alphabet is written , we take input again


## Rock Paper Scissors
Uses dictionary to store what prints out

we use lower and strip to make sure whatever the input is ,if its exact or matches , we use it
otherwise we ask for the input againn

emoticons added for fun and visual appealability

like other codes in this repo.
we use a singular while loop to iterate through it

streak is tracked
and highest streak is tracked as well

Only Time and Random modules are used 

## Word Scramble

we changed the design of this a little 

instead of a while loop
we use a for loop for 5 rounds

and therefore , there's no try again feature

the same difficulty is throughout the 5 rounds

limited words only

used a nested dictionary instead of the if/else logic of adding difficulty seperately 
or creating 3 dictionaries

# THE END