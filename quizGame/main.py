from question_model import Question
from data import anime_data
from quiz_brain import QuizBrain
question_bank = []
for question in anime_data:
    new_question = Question(question["text"],question["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question:
    quiz.next_question()

print("You've compeleted the quiz")
print(f"Your Final Score is: {quiz.score}/{quiz.question_number}")