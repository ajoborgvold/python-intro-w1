import random

weapons = ["rock", "paper", "scissors"]

def play_game():
    computer = random.choice(weapons)
    human = input("Enter your weapon of choice: rock, paper, or scissors\n").strip().lower()

    if computer == human:
        print(f"Computer: {computer}")
        print(f"Human: {human}")
        print("It's a tie!")
    elif computer == "rock" and human == "scissors":
        print(f"Computer: {computer}")
        print(f"Human: {human}")
        print("Computer wins.")
    elif computer == "paper" and human == "scissors":
        print(f"Computer: {computer}")
        print(f"Human: {human}")
        print("Human wins.")
    elif computer == "rock" and human == "paper":
        print(f"Computer: {computer}")
        print(f"Human: {human}")
        print("Human wins.")
    elif computer == "scissors" and human == "paper":
        print(f"Computer: {computer}")
        print(f"Human: {human}")
        print("Computer wins.")
    elif computer == "paper" and human == "rock":
        print(f"Computer: {computer}")
        print(f"Human: {human}")
        print("Computer wins.")
    elif computer == "scissors" and human == "rock":
        print(f"Computer: {computer}")
        print(f"Human: {human}")
        print("Human wins.")
    else:
        print("You chose a weapon that does not exist.")

play_game()