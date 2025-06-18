"""
This script initializes a quiz application using question data and custom classes.

It creates a list of Question objects from the provided question data,
initializes the QuizBrain logic handler, and launches the user interface
for the quiz. After the quiz is completed, it prints the final score.
"""

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface


def create_question_bank(data: list[dict]) -> list[Question]:
    """
    Converts raw question data into a list of Question objects.

    Parameters:
        data (list[dict]): A list of dictionaries containing question text and correct answer.

    Returns:
        list[Question]: A list of Question objects.
    """
    question_bank = []
    for question in data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
    return question_bank


if __name__ == "__main__":
    # Create question bank from data
    question_bank = create_question_bank(question_data)

    # Initialize quiz logic and UI
    quiz = QuizBrain(question_bank)
    quiz_ui = QuizInterface(quiz)

    # Print final score after quiz completion
    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")
