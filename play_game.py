from wordle_script import start_game

# Start a game with a random word
start_game()
# Start a game with a word that is passed in
start_game(pass_word="hinge")
# Start a game with a word that fails the assert
start_game(pass_word="moustache")
