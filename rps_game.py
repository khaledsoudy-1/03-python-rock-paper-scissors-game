import random
import sys


def get_user_choice():
    """Handle user input and ensure it's valid."""
    while True:
        try:
            user = int(input("Please, enter:\n1 for Rock\n2 for Paper\n3 for Scissors\n"))
            
            # Validate user input.
            if user in [1, 2, 3]:
                return user             # Return the valid user choice and stop execution
            raise ValueError            # Raise an error if input is not valid
        
        except ValueError:
            # Inform the user of invalid input and prompt again
            print("\nInvalid input. You must enter 1, 2, or 3.\n")

def decide_winner(player, opponent):
    """Determine the result of the game."""
    if player == 1 and opponent == 3:
        return "🎉🎉 You won!"
    elif player == 2 and opponent == 1:
        return "🎉🎉 You won!"
    elif player == 3 and opponent == 2:
        return "🎉🎉 You won!"
    elif player == opponent:
        return "🤝 Tie Game!"
    else:
        return "😥 You lost .. better luck next time."


def rps_game():
    game_counter = 0
    player_wins = 0
    computer_wins = 0
    
    user = get_user_choice()                   # Get user's choice
    computer = random.choice([1, 2, 3])        # Randomly choose for the computer
    
    # Display the choices
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}\n")
    
    # Determine the result of the game
    result = decide_winner(user, computer)
    
    # Increment game counter
    game_counter += 1
    
    # Increment player_wins and computer_wins
    if result.startswith("🎉"):
        player_wins += 1
    if result.startswith("😥"):
        computer_wins += 1
    
    # Display counters
    print(f"Game Count    : {game_counter}")
    print(f"Player Wins   : {player_wins}")
    print(f"Computer Wins : {computer_wins}\n")
    
    # Display the result of the game
    print(result)
    
    # Ask the user if they want to play again
    print("\nPlay again ?!")
    playagain = input("Y for Yes\nQ to Quit\n").lower().strip()
    
    # Ensure the user enters either 'y' or 'q' for their choice
    while playagain not in ['y', 'q']:
        playagain = input("Y for Yes\nQ to Quit\n").lower().strip()
    
    if playagain == 'y':
        print("\n===== Welcome Back 😍 =====")
        return rps_game()
    
    else:
        print("🎉🎉🎉🎉\nThank you for playing !\nBye 👋")
        sys.exit()


if __name__ == '__main__':
    print("===== Welcome To The RPS Game 🧱📄✂ =====")
    rps_game()
