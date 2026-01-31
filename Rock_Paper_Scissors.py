import random
import logging
logging.basicConfig(level=logging.INFO)

def UI():
    print("========================================")
    print("Welcome to the Rock Paper Scissors game!")
    print("========================================")



def rock_paper_scissors(stop = "yes"):
    while stop == "yes":
        logging.info("Rock Paper Scissors game started!")
        UI()
        my_choice = input("Chose rock, paper, or scissors: ")
        pc_choice = random.choice(["rock", "paper", "scissors"])
        if my_choice == "rock" or my_choice == "paper" or my_choice == "scissors":
            pass
        else:
            logging.warning("user did not enter a valid choice!")
        if my_choice == pc_choice:
            print("It's a tie!")                                #tie
        elif my_choice == "paper" and pc_choice == "rock": #you win
            print("You win!")
        elif my_choice == "rock" and pc_choice == "scissors":   #you win
            print("You win!")
        elif my_choice == "scissors" and pc_choice == "paper":  #you win
            print("You win!")
        elif my_choice == "rock" and pc_choice == "paper":
            print("Computer wins!")
        elif my_choice == "paper" and pc_choice == "scissors":
            print("Computer wins!")
        elif my_choice == "scissors" and pc_choice == "rock":
            print("Computer wins!")
        stop = input("Do you want to play again? (yes/no): ")
        if stop == "yes":
            continue
        else:
            logging.info("game ended!")
            break
rock_paper_scissors("yes")
