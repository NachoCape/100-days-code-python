import imp
import random
from re import A
import hangman_art
import hangman_words

stages = hangman_art.stages

word_list = hangman_words.word_list
print(hangman_art.logo)
word = random.choice(word_list)
list = []
list += ["_"] * len(word)
lives = 6
while "_" in list and lives > 0:
    letter = input("Type a letter ").lower()
    if letter not in word:
            lives -= 1
            print(f"You guessed {letter}, that's not in the \
word. You lose a life.\n{list}\n{stages[lives]}\n")
            continue
    if letter in list:
        print(f"You've already guessed {letter}\n{list}\n{stages[lives]}\n")
        continue
    for i in range(len(word)):
        if word[i] == letter:
            list[i] = letter
    print(f"{list}\n{stages[lives]}\n")
if lives == 0:
    print("You Lose")
else:
    print("You win")
print(word)