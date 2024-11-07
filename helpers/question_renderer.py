# render_question.py
from jinja2 import Environment, FileSystemLoader
import os

# Configure the template environment
env = Environment(loader=FileSystemLoader(os.path.dirname(__file__)))

class QuestionRenderer:
    def __init__(self, question_text, options, is_multiple_choice, question_id="q1"):
        """
        Initializes the renderer for a question (single or multiple choice).

        :param question_text: str, the question text
        :param options: list of dicts, each containing 'label' and 'value' keys for each option
        :param is_multiple_choice: bool, indicates if the question is multiple choice
        :param question_id: str, unique identifier for the question (default "q1")
        """
        self.question_text = question_text
        self.options = options
        self.is_multiple_choice = is_multiple_choice
        self.question_id = question_id

    def render(self):
        """
        Renders the HTML for a question based on the given template.

        :return: str, rendered HTML
        """
        template = env.get_template("templates/question_template.html")
        return template.render(
            question_text=self.question_text,
            options=enumerate(self.options),
            is_multiple_choice=self.is_multiple_choice,
            question_id=self.question_id
        )

# Sample data entries
multiple_choice_data = {
    "question_text": "Which of the following are common types of life insurance policies? (Select all that apply)",
    "options": [
        {"label": "A. Term Life", "value": "A"},
        {"label": "B. Whole Life", "value": "B"},
        {"label": "C. Universal Life", "value": "C"},
        {"label": "D. Variable Life", "value": "D"}
    ],
    "question_id": "q5",
    "is_multiple_choice": True
}

single_choice_data = {
    "question_text": "What is the capital of France?",
    "options": [
        {"label": "A. Paris", "value": "A"},
        {"label": "B. Rome", "value": "B"},
        {"label": "C. Berlin", "value": "C"},
        {"label": "D. Madrid", "value": "D"}
    ],
    "question_id": "q1",
    "is_multiple_choice": False
}

# Render multiple-choice question
multiple_choice_renderer = QuestionRenderer(
    question_text=multiple_choice_data["question_text"],
    options=multiple_choice_data["options"],
    is_multiple_choice=multiple_choice_data["is_multiple_choice"],
    question_id=multiple_choice_data["question_id"]
)
multiple_choice_html = multiple_choice_renderer.render()
print(multiple_choice_html)

# Render single-choice question
single_choice_renderer = QuestionRenderer(
    question_text=single_choice_data["question_text"],
    options=single_choice_data["options"],
    is_multiple_choice=single_choice_data["is_multiple_choice"],
    question_id=single_choice_data["question_id"]
)
single_choice_html = single_choice_renderer.render()
print(single_choice_html)
