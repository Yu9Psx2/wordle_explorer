import pandas as pd
import random
from colorama import init, Fore
from counter_script import lookup_function


def start_game(user_input=True, pass_word=None):
    """Starts a game of Wordle. 
    pass_word is a string to pass to play the game using a specified word
    user_input is a boolean to toggle user_input mode on or off (not yet implemented)
    """
    assert pass_word == None or pass_word.isalpha(), "pass_word is not alpha"
    if pass_word:
        assert len(pass_word) == 5, "pass_word is not 5 letters long"
    # This init has something to do with the font color of the text in the terminal
    init(autoreset=True)
    dataframe = pd.read_csv("wordle_words.csv")
    # put the words into a list
    word_list = dataframe["Unnamed: 0"].values.tolist()
    # Copy the list so that original_list is a list of all words while word_list is a working copy of possible words given the previous guesses
    original_list = word_list.copy()
    # List of words chosen so far
    chosen_words = []
    # Create sets for used letters
    used_white_letters = set()
    used_non_white_letters = set()
    # Get a random word if the passed word is None, otherwise use the passed word as the random word
    if pass_word == None:
        random_word = random.choice(word_list)
    else:
        random_word = pass_word
    # Set a flag for the win condition
    game_won_flag = False

    def refine_available_words(
        current_word,
        used_white_letters,
        used_non_white_letters,
        word_list,
        color_tracker,
    ):
        # This helper function takes the current guess and returns an updated copy of the word_list to reflect the new choices
        # It also returns a bestword that is found using the lookup_function from counter_script.py
        new_list = []
        for i in range(0, len(word_list)):
            temp_word = word_list[i]
            if temp_word == current_word:
                continue
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
        best_word = lookup_function(new_list)[0]
        return new_list, best_word

    def word_selection():
        # a helper function for user word selection
        current_word = input("Choose a word: ")
        while current_word.isalpha() == False or len(current_word) != 5:
            current_word = input(
                "Word needs to be 5 letters and alpha, Choose a word: "
            )
        while current_word not in original_list:
            current_word = input("Not a word, choose again: ")
        return current_word

    # This is the while loop for the game
    while game_won_flag == False and len(chosen_words) < 6:
        if user_input:
            current_word = word_selection()
        else:
            if len(chosen_words) == 0:
                current_word = "irate"
            else:
                current_word = best_word  # throw away word for now
        chosen_words.append(current_word)
        build_word = ""
        color_tracker = []
        # For loop to loop through the guess word and add each letter to the set of letters that are in or not in the random_word
        for i in current_word:
            if i in random_word:
                used_non_white_letters.add(i)
            else:
                used_white_letters.add(i)
        if current_word == random_word:
            if user_input:
                print("You won!")
            game_won_flag = True
        else:
            # For loop to build a colored string in the terminal for the user
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
            # Call the function to get an updated list of possible words and a suggesed best_word to use
            word_list, best_word = refine_available_words(
                current_word,
                used_white_letters,
                used_non_white_letters,
                word_list,
                color_tracker,
            )
            if user_input:
                print(f"This is your chosen word {build_word}")
                print(f"This is the best_word: {best_word}")
                print(
                    f"These are the used up letters: {used_white_letters.union(used_non_white_letters)}\n next guess please:"
                )
    return game_won_flag
