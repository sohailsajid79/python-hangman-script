import random
from hangmanArt import stages, logo
from wordList import words

print(logo)

# Initialize game variables
endOfGame = False # Flag to track whether the game has ended
lives = 6 # Number of lives the player has

# Choose a random word from the list
choosenWord = random.choice(words)

# Determine the length of the chosen word
wordLength = len(choosenWord)

# Create a list to represent the display of the word with underscores
display = ["_" for _ in range(wordLength)]

# Start the main game loop
while not endOfGame:
    # Get a letter guess from the player
    guess = input("guess a letter: ").lower()
    
    # Check if the guessed letter has already been guessed
    if guess in display:
        print(f"you've already guessed {guess}")
    
    # Flag to track whether the guessed letter is correct
    correct_guess = False
    
    # Iterate through each position in the chosen word
    for position in range(wordLength):
        # Initial position is 0
        letter = choosenWord[position]
        if letter == guess:
            # Check if the letter at the current position matches the guessed letter (guess), 
            # it updates the corresponding position in the display list with the guessed letter.
            display[position] = letter
            correct_guess = True # Set the flag to indicate a correct guess
        
    # Check if the guessed letter is incorrect and not in the chosen word
    if not correct_guess and guess not in choosenWord:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        # Check if the player has run out of lives
        if lives == 0:
            endOfGame = True
            print(f"you lose! the word was {choosenWord}")
           
    # Print the current state of the word display        
    print(*display, sep="")
    
    # Check if all letters have been guessed (no underscores remaining)
    if "_" not in display:
        endOfGame = True
        print(f"you win! the word was {choosenWord}")
    
    # Print the current state of the hangman based on remaining lives
    print(stages[lives])