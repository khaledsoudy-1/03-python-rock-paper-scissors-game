import random

print("===== Welcome To The RPS Game 🧱📄✂ =====")

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