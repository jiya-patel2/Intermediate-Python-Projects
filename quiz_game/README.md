cat << 'EOF' > README.md
# ⛩️ Anime Quiz Project

A modular, Object-Oriented Python application that quizzes users on their anime knowledge. The project follows the **MVC (Model-View-Controller)** pattern to separate data logic from user interaction.



## ## 🚀 Features
* **Dynamic Question Bank**: Automatically generates a list of `Question` objects from raw data.
* **Quiz Logic**: Managed by `QuizBrain`, which tracks scores, question numbers, and game status.
* **Modular Design**: Separates the data (`anime_data`), the model (`Question`), and the controller (`QuizBrain`).

---

## ## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/jiya-patel2/quizGame.git](https://github.com/jiya-patel2/quizGame.git)

2. **Ensure all files are in the same directory:**
    * main.py (Your entry point)
    * question_model.py
    * quiz_brain.py
    * data.py

3. **Run the quiz:**
python 
    ```bash 
    main.py

## ## **💻 Project Structure**
    Question Class: A simple blueprint for holding the text and the correct answer.
    anime_data: A list of dictionaries containing the quiz questions.
    QuizBrain: The "engine" of the game. It handles:
    next_question(): Asks the user the next question.
    check_answer(): Validates input and updates the score.
    still_has_questions(): Checks if the quiz is finished.