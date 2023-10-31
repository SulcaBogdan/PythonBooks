import random

choose = ["Rock", "Paper", "Scissors"]
question = input("Wanna play rock/paper/scissors?")
while question == "yes":
    computer_choice = random.choice(choose)
    choice = input("What do you choose? Rock, Paper or Scissors?:")
    if computer_choice == choice:
        print(f"You choose {choice} and the computer choose {computer_choice}")
        print("Tie")
    elif choice == "Rock" and computer_choice == "Scissors":
        print(f"You choose {choice} and the computer choose {computer_choice}")
        print("You win!")
    elif choice == "Scissors" and computer_choice == "Paper":
        print(f"You choose {choice} and the computer choose {computer_choice}")
        print("You win!")
    elif choice == "Paper" and computer_choice == "Rock":
        print(f"You choose {choice} and the computer choose {computer_choice}")
        print("You win!")
    else:
        print(f"You choose {choice} and the computer choose {computer_choice}")
        print("You lose")
    continue_q = input("Do you want to try again?")
    if continue_q == "no":
        question = "no"
