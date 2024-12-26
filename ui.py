from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=50, pady=20, background=THEME_COLOR)
        # label
        self.score = Label(text="Score: ", fg="white", bg=THEME_COLOR, font=("Arial", 15, "normal"))
        self.score.grid(row=0, column=1)
        # create the canvas

        # setup canvas and text
        self.canvas = Canvas(width=300, height=300)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="", font=FONT)
        self.canvas.itemconfig(self.question_text, text="")

        # setup buttons
        TRUE_IMG = r"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"
        FALSE_IMG = r"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"

        true_img = PhotoImage(data=TRUE_IMG)
        false_img = PhotoImage(data=FALSE_IMG)

        self.true = Button(image=true_img, highlightthickness=0, command=self.correct)
        self.true.grid(row=2, column=0)
        self.false = Button(image=false_img, highlightthickness=0, command=self.false)
        self.false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}/12")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You reached the end of this quiz.")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def correct(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        elif not is_right:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)
