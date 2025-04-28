import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

# Main function for the game
def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        # Get user input
        user_choice = input("Enter 'rock', 'paper', or 'scissors': ").lower()
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        # Computer selects randomly
        computer_choice = random.choice(["rock", "paper", "scissors"])
        
        # Determine the winner
        result = determine_winner(user_choice, computer_choice)
        
        # Display the choices and the result
        print(f"Your choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        print(result)
        
        # Update score
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        
        # Display current score
        print(f"Your score: {user_score} | Computer score: {computer_score}")
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

# Start the game
if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    play_game()
