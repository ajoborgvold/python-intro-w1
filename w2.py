'''
Game refactoring:
    1) Create a weapons_dict -> DONE!
    2) Create a play_game function -> DONE!
    3) Initialize human_score and computer_score to 0 -> DONE!
    4) Create a while loop -> DONE!
    5) Get a random number using random.randint(1,3) and convert it to a string -> DONE!
    6) Initialize computer_weapon to a random weapon using the random number -> DONE!
    7) Get a user input -> DONE!
    8) Check if the user input matches a key in the weapons_dict -> DONE!
    9) Initialize human_weapon to the selected weapon -> DONE!
    10) Compare the human_weapon and the computer_weapon and increase the score of the winning part -> DONE!
    11) Print the overall winner

Weapon hierarchy:
    rock > scissors
    paper > rock
    scissors > paper
'''

import random

weapons_dict = {"1": "rock", "2": "paper", "3": "scissors"}

def play_game():
    human_score = 0
    computer_score = 0
    
    while human_score + computer_score < 3:        
        random_num = str(random.randint(1,3))
        computer_weapon = weapons_dict[random_num]
        
        print("Select a weapon:")
        print("1) Rock")
        print("2) Paper")
        print("3) Scissors")
        human_input = input("Enter a number between 1 and 3: ")
        
        if human_input not in weapons_dict.keys():
            print("Invalid input. Please try again.")
            continue
        
        human_weapon = weapons_dict[human_input]
        
        if human_weapon == computer_weapon:
            print(f"Human: {human_weapon}")
            print(f"Computer: {computer_weapon}")
            print("It's a tie.")
        elif human_weapon == "rock":
            if computer_weapon == "paper":
                print(f"Human: {human_weapon}")
                print(f"Computer: {computer_weapon}")
                computer_score += 1
                print(f"Human score: {human_score}. Computer score: {computer_score}")
            elif computer_weapon == "scissors":
                print(f"Human: {human_weapon}")
                print(f"Computer: {computer_weapon}")
                human_score += 1
                print(f"Human score: {human_score}. Computer score: {computer_score}")
        elif human_weapon == "paper":
            if computer_weapon == "rock":
                print(f"Human: {human_weapon}")
                print(f"Computer: {computer_weapon}")
                human_score += 1
                print(f"Human score: {human_score}. Computer score: {computer_score}")
            elif computer_weapon == "scissors":
                print(f"Human: {human_weapon}")
                print(f"Computer: {computer_weapon}")
                computer_score += 1
                print(f"Human score: {human_score}. Computer score: {computer_score}")
        elif human_weapon == "scissors":
            if computer_weapon == "rock":
                print(f"Human: {human_weapon}")
                print(f"Computer: {computer_weapon}")
                computer_score += 1
                print(f"Human score: {human_score}. Computer score: {computer_score}")
            elif computer_weapon == "paper":
                print(f"Human: {human_weapon}")
                print(f"Computer: {computer_weapon}")
                human_score += 1
                print(f"Human score: {human_score}. Computer score: {computer_score}")
    
    if human_score < computer_score:
        print("Computer won!")
    elif human_score > computer_score:
        print("Human won!")
    else:
        print("No winner")
        
        
play_game()
