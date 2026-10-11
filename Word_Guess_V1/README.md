# HANGMAN

Word Guessing Game :
random words are given

one of them is selected 

we get 6 guesses
one letter at a time

6 stages of hangman are shown.

## How code works
Words are stored in a list
stages of hangman are stored in a list
time.sleep is used between outputs
random module is used to select a random word from the list
While Loop is used to iterate through all guesses
"_" is shown for every unguessed letter
strip and lower are used when taking input from user incase they press "Space" or a capital letter
if more letters or a non-alphabet is written , we take input again
