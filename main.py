
import random
import hangman_art
import hangman_words


end_of_game = False
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


print(hangman_art.logo)



display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for p in range(word_length):
        letter = chosen_word[p]
        if letter == guess:
            print(hangman_art.stages[lives])
            display[p] = letter
            print(f"{' '.join(display)}")

        
    if guess not in chosen_word:
        lives -= 1
        if lives > 0:
            print(hangman_art.stages[lives])
            print(f"{' '.join(display)}")
        else:
            print(hangman_art.stages[lives])
            print("You lose")
            print(f'Pssst, the solution is {chosen_word}.')
            end_of_game = True

        if "_" not in display:
            end_of_game = True
            print("You win.")
