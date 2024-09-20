import random
import sys


def rps_game():
    user = int(input("Please, enter:\n1 for Rock\n2 for Paper\n3 for Scissors\n"))
    computer = random.choice([1, 2, 3])
    
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}\n")
    
    if user == 1 and computer == 3:
        print("🎉🎉 You won!")
    elif user == 2 and computer == 1:
        print("🎉🎉 You won!")
    elif user == 3 and computer == 2:
        print("🎉🎉 You won!")
    elif user == computer:
        print("🤝 Tie Game!")
    else:
        print("😥 You lost .. better luck next time.")
    
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
