from wordle_script import start_game

# With the actual wordle game complete in the wordle_script file,
# I can start programming some options for playability.
# I haven't done much with importing my own scripts, but this is a start
# Right now the game is forcing you to play optimally by forcing to choose words without any used white chars

# Start a game with a random word
start_game()
# Start a game with a word that is passed in
start_game(pass_word="hinge")

start_game(user_input=False)
# Start a game with a word that fails the assert
start_game(pass_word="moustache")
