import random
import sys


def get_user_choice():
    """Handle user input and ensure it's valid."""
    while True:
        try:
            user = int(input("Please, enter:\n1 for Rock\n2 for Paper\n3 for Scissors\n"))
            
            # Validate user input.
            if user in [1, 2, 3]:
                return user             # <== NOTE that we return the user value
            raise ValueError
        
        except ValueError:
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
    user = get_user_choice()
    computer = random.choice([1, 2, 3])
    
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}\n")
    
    result = decide_winner(user, computer)
    print(result)
    
    print("\nPlay again ?!")
    playagain = input("Y for Yes\nQ to Quit\n").lower().strip()
    
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
