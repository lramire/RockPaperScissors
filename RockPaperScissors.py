import random

print("Welcome to Rock Paper Scissors! ")

while True:
    user_choice = input("Please make a selection (rock, paper, or scissors): ")
    possible_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(possible_choices)
    print(f" \n Your selection was {user_choice},  Your opponent's selection was {computer_choice}")
 #turn if into a while loop until comp and user don't tie, then break
    while user_choice == computer_choice:
        print(f"Both players chose {user_choice}, tie game")
        user_choice = input("Please make a selection (rock, paper, or scissors): ")
        computer_choice = random.choice(possible_choices)
        if user_choice != computer_choice:
            break
    #Make it so if its a tie both players choose again
    if user_choice == "paper":
        if computer_choice  == "rock":
            print("Paper covers Rock! You Win!")
        else:
            print("Scissors cuts paper, you lose")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You Win!")
        else:
            print("Paper covers rock, you lose")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper, you win")
        else:
            print("Rock smashes scissors, you lose")
    print("Thank you for playing")
    play_again = input("Would you like to play again? (y/n): ")
    if play_again.lower() != "y":
        break



    




