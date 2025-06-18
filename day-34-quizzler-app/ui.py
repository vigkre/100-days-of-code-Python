from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    """
    A graphical user interface for the quiz application using tkinter.

    This class handles the display of quiz questions, score updates,
    and user interactions through True/False buttons.
    """

    def __init__(self, quiz_brain: QuizBrain):
        """
        Initializes the QuizInterface with the given QuizBrain instance.

        Parameters:
            quiz_brain (QuizBrain): An instance of QuizBrain to manage quiz logic.
        """
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)        
        self.quiz_text = self.canvas.create_text(
            150, 125, text="Quiz question goes here", width=280, fill=THEME_COLOR, font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        # Add wrong and right button with images
        false_img = PhotoImage(file="day-34-quizzler-app/images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_answer)
        self.false_button.grid(row=2, column=1)

        true_img = PhotoImage(file="day-34-quizzler-app/images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_answer)
        self.true_button.grid(row=2, column=0)
        
        self.display_next_question()

        self.window.mainloop()

    def display_next_question(self) -> None:
        """
        Retrieves and displays the next question from the quiz.

        Updates the score and disables buttons if the quiz is finished.
        """
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_text, text="You've reached the end of the game!!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def false_answer(self) -> None:
        """
        Handles the event when the user selects 'False' as their answer.
        """     
        self.give_feedback(self.quiz.check_answer(user_answer="False"))

    def true_answer(self) -> None: 
        """
        Handles the event when the user selects 'True' as their answer.
        """          
        self.give_feedback(self.quiz.check_answer(user_answer="True"))
        
    def give_feedback(self, is_right: bool) -> None:
        """
        based on whether the user's answer was correct.

        Parameters:
            is_right (bool): True if the user's answer was correct, False otherwise.
        """
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.display_next_question)
