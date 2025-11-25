import random
from hangman_art import logo, stages
from words import get_words, get_difficulty

difficulty = get_difficulty()
word_list = get_words(difficulty)

print(logo)
print("Welcome to Hangman Game!")

chosen_word = random.choice(word_list)
display = ["_"] * len(chosen_word)

# Lives depend on difficulty
lives = 6 if difficulty == "easy" else 5 if difficulty == "medium" else 4


guessed_letters = []

print(f"\nYou selected: {difficulty.capitalize()}")
print(f"The word has {len(chosen_word)} letters.\n")

#---------GAME LOOP---------#

while "_" in display and lives >= 0:

    print("Word:", " ".join(display))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter \n")
        continue

    guessed_letters.append(guess)


    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess

    else:
        print("❌Wrong guess")
        lives -= 1

    print(stages[lives])
    print(f"Lives left : {lives}\n")


    if lives == 0:
        print(f"You lose!! The word was: {chosen_word}")
        break


if "_" not in display:
    print("You win🎉")
    print(f"The word was: {chosen_word}")