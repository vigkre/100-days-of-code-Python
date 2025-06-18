from question_model import Question
import html


class QuizBrain:
    """
    Manages the quiz logic including question progression, scoring, and answer validation.
    """

    def __init__(self, q_list: list[Question]):
        """
        Initializes the QuizBrain instance.

        Parameters:
            q_list (list[Question]): A list of Question objects for the quiz.
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self) -> bool:
        """
        Checks if there are more questions left in the quiz.

        Returns:
            bool: True if there are remaining questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        """
        Retrieves the next question in the quiz and increments the question counter.

        Returns:
            str: The formatted question string.
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text: str = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer: str) -> bool:
        """
        Validates the user's answer against the correct answer.

        Parameters:
            user_answer (str): The answer provided by the user.

        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        correct_answer: str = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
