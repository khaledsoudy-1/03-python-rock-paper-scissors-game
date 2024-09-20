# 🎮 Rock-Paper-Scissors Game

## 📖 Description

Experience the classic game of Rock-Paper-Scissors in this sleek Python implementation. Challenge the computer in a battle of wits and strategy!

## 🏆 Game Rules

- 🪨 Rock crushes ✂️ Scissors
- ✂️ Scissors cuts 📄 Paper
- 📄 Paper covers 🪨 Rock
- If both players choose the same option, it's a tie!

## 🚀 How to Play

1. Ensure you have Python installed on your system.
2. Run the game using the command: `python rock_paper_scissors.py`
3. Make your choice by entering:
   - `1` for Rock 🪨
   - `2` for Paper 📄
   - `3` for Scissors ✂️
4. Watch as the computer makes its move.
5. See the result and your updated score.
6. Choose to play again or exit the game.

## 💻 Code Highlights

### Enum Class
We use Python's `Enum` class to represent game choices:

```python
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
```

This enhances code readability and maintainability by using meaningful names instead of magic numbers.

## 🧠 Strategy Tips

- Observe patterns in the computer's choices to gain an edge.
- Mix up your choices to keep the computer guessing.
- Remember, in the long run, a truly random strategy is often the best!

## 🛠️ Future Enhancements

- Implement a GUI for a more interactive experience.
- Add difficulty levels for the computer player.
- Include a leaderboard to track high scores.

## 👨‍💻 Author

Khaled Soudy

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you encounter any problems or have any questions, please open an issue in the GitHub repository.

---

Enjoy the game and may the odds be ever in your favor! 🍀
