import html
class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.correct_answer = current_question.answer
        # FIX: decode HTML entities
        question_text = html.unescape(current_question.text)
        return f"Q.{self.question_number} {question_text}"
        # answer = input(f"Q.{self.question_number} {question_text} (True/False): ")
        # self.check_answer(answer,current_question.answer)
        

    def check_answer(self,answer):
        if answer.lower() == self.correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
       