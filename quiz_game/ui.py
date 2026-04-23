from tkinter import *
from quiz_brain import *
THEME_COLOR = "#3E2D68"
CANVAS_COLOR = "#8D74D1"
FONT_COLOR = "#FFFFFF"
class AnimeQuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Anime Quiz")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_label = Label(text=f"Score : 0",fg=FONT_COLOR,bg=THEME_COLOR)
        self.score_label.grid(row=0,column=1)
        self.canvas = Canvas(width= 300, height=250 , bg=CANVAS_COLOR, highlightthickness=0)
        self.question_text = self.canvas.create_text(150,125,text=f"question",font=("Arial",20 , "italic"),width=250, fill=FONT_COLOR)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        right_img = PhotoImage(file= "right.png")
        self.right_button = Button(image=right_img, highlightthickness=0,command=self.true_pressed)
        self.right_button.grid(row=2,column=0)

        wrong_img = PhotoImage(file= "wrong.png")
        self.wrong_button = Button(image=wrong_img, highlightthickness=0,command=self.false_pressed)
        self.wrong_button.grid(row=2,column=1)
        
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg= CANVAS_COLOR)
        if self.quiz.still_has_question():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text=f"Score: {self.quiz.score}")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    
    def false_pressed(self): 
        is_right = self.quiz.check_answer("False")   
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg= "green")
        else:
            self.canvas.config(bg= "red")
        self.window.after(1000,self.get_next_question)
       