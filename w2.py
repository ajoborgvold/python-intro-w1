'''
Game refactoring:
    1) Create a weapons_dict
    2) Create a play_game function
    3) Initialize human_score and computer_score to 0
    4) Create a while loop
    5) Get a random number using random.randint(1,3) and convert it to a string
    6) Initialize computer_weapon to a random weapon using the random number
    7) Get a user input
    8) Check if the user input matches a key in the weapons_dict
    9) Initialize human_weapon to the selected weapon
    10) Compare the human_weapon and the computer_weapon and increase the score of the winning part
    11) Print the overall winner

Weapon hierarchy:
    rock > scissors
    paper > rock
    scissors > paper
'''
