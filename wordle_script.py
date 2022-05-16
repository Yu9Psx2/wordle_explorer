import pandas as pd
import random
from colorama import init, Fore

init(autoreset=True)


dataframe = pd.read_csv("wordle_words.csv")

word_list = dataframe["Unnamed: 0"].values.tolist()

chosen_words = []
used_white_letters = set()
used_non_white_letters = set()
random_word = random.choice(word_list)
game_won_flag = False
print(random_word)


def refine_available_words(
    current_word, used_white_letters, used_non_white_letters, word_list, color_tracker
):
    new_list = []
    for i in range(0, len(word_list)):
        temp_word = word_list[i]
        flag = True
        pointer = 0
        while pointer < 5 and flag == True:
            if temp_word[pointer] in used_white_letters:
                flag = False
            if color_tracker[pointer] == "G":
                if current_word[pointer] != temp_word[pointer]:
                    flag = False
            elif color_tracker[pointer] == "Y":
                if current_word[pointer] not in temp_word:
                    flag = False
            pointer += 1
        if flag == True:
            new_list.append(temp_word)

    return new_list, "Holder for best word"


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
    color_tracker = []
    for i in current_word:
        if i in random_word:
            used_non_white_letters.add(i)
        else:
            used_white_letters.add(i)
    if current_word == random_word:
        print("You won!")
        game_won_flag = True
    else:
        for i in range(0, 5):
            if current_word[i] == random_word[i]:
                build_word = build_word + Fore.GREEN + current_word[i]
                color_tracker.append("G")
            elif current_word[i] in random_word:
                build_word = build_word + Fore.YELLOW + current_word[i]
                color_tracker.append("Y")
            else:
                build_word = build_word + Fore.WHITE + current_word[i]
                color_tracker.append("W")
        print(f"This is your chosen word {build_word}")
        word_list, best_word = refine_available_words(
            current_word,
            used_white_letters,
            used_non_white_letters,
            word_list,
            color_tracker,
        )
        print(f"This is the length of word list {len(word_list)}")
        print(word_list)
        print(
            f"These are the used up letters: {used_white_letters.union(used_non_white_letters)}\n next guess please:"
        )

