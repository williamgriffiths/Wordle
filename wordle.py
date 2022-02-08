from define import define
import random

guesslist = open('guesses.txt').read().splitlines()
answers = open('words.txt').read().splitlines()
word = random.choice(answers)

guesses = 6
won = False

alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(guesses):
    guess = input("Guess {}: ".format(i+1)).lower()
    if guess not in guesslist:
        print("Not a valid word!\n")
    if guess == word:
        won = True
        print("CONGRATS!")
        print("Word was: {}".format(word))
        break
    else:
        hint = ""
        for j in range(len(guess)):
            if guess[j] in word:
                if word[j] == guess[j]:
                    hint += "\u0332".join("Y ").strip()
                else:
                    hint += "Y"
                alphabet = alphabet.replace(guess[j],"\u0332".join(guess[j]+" ").strip())
            else:
                hint += "N"
                alphabet = alphabet.replace(guess[j],'#')
            
    if guess in guesslist:
        print(hint)
        print(alphabet + "\n")

    if i == 4:
        define(word)
        print("\n")

    guesses -= 1


if won == False:
    print("PATHETIC!")
    print("Word was: {}".format(word))
