from wordle_script import start_game

# play several games at once and return number of winning games, runs slowly

counter = 0

for i in range(0, 200):
    temp = start_game(user_input=False)
    if temp:
        counter += 1

print(counter)
