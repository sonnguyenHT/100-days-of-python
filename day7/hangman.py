import random
import hangman_words

live = 6 #  I use this variable instead of code a lot of Hangman

list_letter = hangman_words.list_letter
letter = random.choice(list_letter)

guess_string = ""
for x in range(len(letter)):
    guess_string += "_"
print(guess_string)

while True:
    guess_character = input("Guess a letter :")[0].lower()
    if letter.__contains__(guess_character) :
        for x in range(len(letter)):
            if letter[x] == guess_character:
                guess_string = guess_string[:x] + guess_character + guess_string[(x+1):]  ## replace guess_string[x] with guess_character
        print(guess_string)
        if guess_string == letter:
            print("Done!")
            break
        else:
            continue
    else:
        live -= 1
        print(f'You only have {live} lives')
        if live ==0 :
            print("You die!")
            exit()