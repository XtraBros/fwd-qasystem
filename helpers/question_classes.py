# quiz_module.py

class Question:
    def __init__(self, question_text, options=None):
        """
        Parent class for a quiz question.

        :param question_text: str, The text of the question
        :param options: list, The list of possible answers (default is None)
        """
        self.question_text = question_text
        self.options = options if options is not None else []
        self.template_path = None  # This will be set in each child class

    def load_template(self):
        """
        Returns the path of the HTML template to use for this question type.
        
        :return: str, path to the HTML template
        """
        if self.template_path:
            return self.template_path
        else:
            raise NotImplementedError("Template path not defined for this question type.")


class SingleChoiceQuestion(Question):
    def __init__(self, question_text, options):
        """
        A single-choice question where only one answer can be selected.

        :param question_text: str, The text of the question
        :param options: list, The list of possible answers
        """
        super().__init__(question_text, options)
        self.template_path = "templates/single_choice.html"  # Path to the HTML template for single choice questions
        self.correct_answer = None  # Add correct answer tracking if needed

    def set_correct_answer(self, answer):
        """
        Set the correct answer for this single-choice question.
        
        :param answer: str, the correct answer
        """
        if answer in self.options:
            self.correct_answer = answer
        else:
            raise ValueError("Answer not in options")


class MultipleChoiceQuestion(Question):
    def __init__(self, question_text, options):
        """
        A multiple-choice question where multiple answers can be selected.

        :param question_text: str, The text of the question
        :param options: list, The list of possible answers
        """
        super().__init__(question_text, options)
        self.template_path = "templates/multiple_choice.html"  # Path to the HTML template for multiple choice questions
        self.correct_answers = []  # List to track multiple correct answers

    def add_correct_answer(self, answer):
        """
        Add a correct answer for this multiple-choice question.

        :param answer: str, one of the correct answers
        """
        if answer in self.options:
            self.correct_answers.append(answer)
        else:
            raise ValueError("Answer not in options")
