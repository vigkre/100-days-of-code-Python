class Question:
    """
    Represents a single quiz question with its text and correct answer.
    """

    def __init__(self, q_text: str, q_answer: str):
        """
        Initializes a Question instance.

        Parameters:
            q_text (str): The text of the question.
            q_answer (str): The correct answer to the question.
        """
        self.text = q_text
        self.answer = q_answer
