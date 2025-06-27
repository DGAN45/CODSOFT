import random

def play_rock_paper_scissors():
    """Plays a game of Rock, Paper, Scissors."""

    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    user_choice = ""

    while user_choice not in options:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in options:
            print("Invalid choice. Please try again.")

    print("You chose {user_choice}")
    print("Computer chose {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    play_rock_paper_scissors()