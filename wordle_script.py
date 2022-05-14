import pandas as pd
import random
from colorama import init, Fore

init(autoreset=True)


dataframe = pd.read_csv("wordle_words.csv")

word_list = dataframe["Unnamed: 0"].values.tolist()

chosen_words = []
used_letters = []
random_word = random.choice(word_list)
game_won_flag = False
print(random_word)


def word_selection():
    current_word = input("Choose a word: ")
    while current_word not in word_list:
        current_word = input("Not a word, choose again: ")
    while current_word.isalpha() == False or len(current_word) != 5:
        current_word = input("Word needs to be 5 letters and alpha, Choose a word: ")
    return current_word


while game_won_flag == False and len(chosen_words) < 6:
    current_word = word_selection()
    chosen_words.append(current_word)
    build_word = ""
    for i in current_word:
        if i not in used_letters:
            used_letters.append(i)
    if current_word == random_word:
        print("You won!")
        game_won_flag = True
    else:
        for i in range(0, 5):
            if current_word[i] == random_word[i]:
                build_word = build_word + Fore.GREEN + current_word[i]
            elif current_word[i] in random_word:
                build_word = build_word + Fore.YELLOW + current_word[i]
            else:
                build_word = build_word + Fore.WHITE + current_word[i]
        print(f"This is your chosen word {build_word}")
        print(f"These are the used up letters: {used_letters}\n next guess please:")

