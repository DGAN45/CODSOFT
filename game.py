import random

def play_round():
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    user_choice = ""

    # Ask for valid input
    while user_choice not in options:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in options:
            print(" Invalid choice. Please try again.")

    print("\n You chose: {user_choice}")
    print(" Computer chose: {computer_choice}")

    # Determine result
    if user_choice == computer_choice:
        print(" It's a tie!")
        return "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print(" You win!")
        return "user"
    else:
        print(" Computer wins!")
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0

    print(" Welcome to Rock, Paper, Scissors!")
    
    while True:
        result = play_round()
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        print(f"\n Score => You: {user_score} | Computer: {computer_score}")

        play_again = input("\n Do you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print(" Thanks for playing!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
