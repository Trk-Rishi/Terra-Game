import random
import time

words = [
    "tanmay","rishikesh","whatsapp","instagram","hello","python","coding","hangman","welcome"
]


##HANGMAN STAGES ---> From zero(start) to six(end)

hangman = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """
]

print("Welcome to Hangman!!!")
time.sleep(1)
print("Guess the hidden word one letter at a time. ")
time.sleep(1)
print("You have 6 incorrect guesses.")
time.sleep(1)
print("Good luck!!!")
time.sleep(2)

##Selcitng the word for hangman 

word = random.choice(words)


guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6



while True:

   
    print(hangman[wrong_guesses])

    
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word = display_word + letter + " "
        else:
            display_word = display_word + "_ "

    print("Word:", display_word)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    print("Guessed letters:", guessed_letters)

    guess = input("Enter a letter: ").lower().strip()

    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        time.sleep(1)
        continue

    
    if guess in guessed_letters:
        print("You have already guessed that letter!")
        time.sleep(1)
        continue

   
    guessed_letters.append(guess)

    
    if guess in word:
        print("Correct guess!")
        time.sleep(1)
    else:
        wrong_guesses = wrong_guesses + 1
        print("Wrong guess!")
        time.sleep(1)

    
    word_guessed = True

    for letter in word:
        if letter not in guessed_letters:
            word_guessed = False

    
    if word_guessed:
        print("The word was:", word)
        time.sleep(1)
        print("Congratulations! You won!")
        break
    elif wrong_guesses == max_wrong_guesses:
        print(hangman[wrong_guesses])
        print("You ran out of guesses!")
        time.sleep(1)
        print("The correct word was:", word)
        print("Better luck next time!")
        break

time.sleep(1)
print("Thanks for playing Hangman!")