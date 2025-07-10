import random
import requests
from functions import char_in_word
from art import hangman_pics, hangman_intro, hangman_game_over

try:
    response = requests.get('https://random-word-api.herokuapp.com/word')
    data = response.json()
    secret_word = data[0]
except requests.exceptions.RequestException as e:
    print(f"Fehler bei der Anfrage: {e}")

word_list = []
word_char = char_in_word(word = secret_word, list_append = word_list)
life = 6
display_word = ['_'] * len(secret_word)
length_word = len(secret_word)
is_game_over = False
player_inputs = []

print(hangman_intro)
print(f"Welcome to Hangman!\nThe secret word is {length_word} letters long.")
print (hangman_pics[0])

while is_game_over == False:
    print(display_word)
    print(f"These are your guesses: {player_inputs}")
    player_guess = input("Guess a character: ").lower().strip()
    if player_guess in player_inputs:
        print("You already guessed that character.")
        continue
    elif player_guess not in player_inputs:
        player_inputs.append(player_guess)
        if player_guess in word_list:
            for i in range(len(secret_word)):
                char = secret_word[i]
                if player_guess == char:
                    display_word[i] = char
                    if "_" not in display_word:
                        result = "".join(display_word)
                        print(f"You did it, well done! The secret word was: {secret_word}")
                        is_game_over = True
                    else:
                        continue
        else:
            life -=1
            print(f"Life: {life}")
            if life == 5:
                print (hangman_pics[1])
            elif life == 4:
                print (hangman_pics[2])
            elif life == 3:
                print (hangman_pics[3])
            elif life == 2:
                print(hangman_pics[4])
            elif life == 1:
                print(hangman_pics[5])
            elif life == 0:
                print(hangman_pics[6])
                print(hangman_game_over)
                print(f"The secret word was: {secret_word}")
                is_game_over = True