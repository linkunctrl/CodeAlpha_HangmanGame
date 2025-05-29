import random

words = ["sauce", "codealpha", "naruto", "tree", "seafood"]
chosen_word = random.choice(words)
guesses = "" # tracks guesses in a string
tries = 6
# main loop to continue as long as the player has tries left
while tries > 0:
    failed = 0 # counts letters that still need to be guessed
    
    for letter in chosen_word:
        if letter in guesses:
            print(letter, end=" ") #shows letter if guessed
        else:
            print("_", end=" ") # shows underscore if NOT guessed
            failed += 1 # increments failed
    print("")
    # if no missing letters are left
    if failed == 0:
        print("You've won! The word was: ", chosen_word)
        break
    # input the guess
    guess = input("Enter a letter: ").lower()

    # check if letter has already been guessed
    if guess in guesses:
        print("You've already guessed that bozo.")
        continue
    # prints error if player enters more than one letter or a non-letter value
    if not guess.isalpha() or len(guess) != 1:
        print("Enter only one letter.")
        continue

    guesses += guess
    # if guess is not in the word then reduce number of tries
    if guess not in chosen_word:
        tries -= 1
        print("You guessed it wrong.")
        print("You have ", tries, " left.")
    print("")

# Game Over
if tries == 0:
    print("You lost... The word was:", chosen_word)
