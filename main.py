import random
from hangman_art import stages
from hangman_words import random_words as word_list

chosen_word = random.choice(word_list)
lives = 6

#Create blanks
display = []
for _ in range(len(chosen_word)):
    display.append("_")

end_of_game = False
list_of_guesses = []

while not end_of_game:
    guess = input("Please guess a letter: ").lower()

    while guess in list_of_guesses:
        guess = input("You have already guessed that letter. Please enter a new letter: ").lower()
    list_of_guesses.append(guess)

    #Checked guessed letter
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])

    #Print current progress
    print(display)

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You've won!")
    elif lives == 0:
        end_of_game = True
        print("You lose.")

#Join all the elements in the list and turn it into a String.
print(f"{' '.join(display)}")