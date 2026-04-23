from question_model import Question
from data import anime_data
from quiz_brain import QuizBrain
from ui import AnimeQuizInterface

question_bank = []

for question in anime_data:
    new_question = Question(question["question"],question["correct_answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = AnimeQuizInterface(quiz)


print("You've compeleted the quiz")
print(f"Your Final Score is: {quiz.score}/{quiz.question_number}")