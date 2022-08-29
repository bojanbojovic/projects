from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quizBrain: QuizBrain):
        self.quiz = quizBrain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR)
        self.window.config(padx=50, pady=50)

        self.score = Label(text="score: 0", bg=THEME_COLOR, fg="white", pady=10)
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300)
        self.question = self.canvas.create_text(150, 125, width=280 ,text="text", fill="black", font=("Arial", 15, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.wrongImage = PhotoImage(file="false.png")
        self.wrongButton = Button(image=self.wrongImage, command=self.wrong, highlightthickness=0)
        self.wrongButton.grid(row=2, column=0)

        self.rightImage = PhotoImage(file="true.png")
        self.rightButton = Button(image=self.rightImage, command=self.right, highlightthickness=0)
        self.rightButton.grid(row=2, column=1)

        self.scoreNumber = 0

        self.getNextQuestion()

        self.window.mainloop()



    def wrong(self):
        answer = self.quiz.check_answer("False")
        if answer == True:
            self.canvas.config(bg="green")
            self.scoreNumber += 1
        else:
            self.canvas.config(bg="red")

        self.countDown(1)

    def right(self):
        answer = self.quiz.check_answer("True")
        if answer == True:
            self.canvas.config(bg="green")
            self.scoreNumber += 1
        else:
            self.canvas.config(bg="red")

        self.countDown(1)

    def countDown(self, count):
        if count > 0:
            self.window.after(1000, self.countDown, count - 1)
        else:
            self.getNextQuestion()

    def getNextQuestion(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"score: {self.scoreNumber}")
            qText = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=qText)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz.")
            self.rightButton.config(state=" disabled")
            self.wrongButton.config(state="disabled")
