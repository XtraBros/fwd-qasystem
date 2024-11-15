import requests
from bs4 import BeautifulSoup
import json
import re

# Working scrapper for CMFAS exam website and IIQE database website. Only correct answers cannot be fetched.
# URL of the page with quiz questions
url = "https://iiqedatabase.com/iiqe-paper-6-english-preview/"

# Send a request to the URL
response = requests.get(url)
if response.status_code != 200:
    print("Failed to retrieve the page")
    exit()

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Initialize a list to store all quiz data
all_quiz_data = []

# Find all questions within elements with class 'wpProQuiz_listItem'
quiz_items = soup.find_all('li', class_='wpProQuiz_listItem')

# Loop through each quiz item to extract question data
for index, item in enumerate(quiz_items, start=1):
    # Extract question text
    question_text = item.find('div', class_='wpProQuiz_question_text').get_text(strip=True)
    
    # Extract options
    options = []
    option_elements = item.find_all('li', class_='wpProQuiz_questionListItem')
    for option in option_elements:
        option_text = option.get_text(strip=True)
        options.append(option_text)

    # Identify the correct answer by checking for 'wpProQuiz_answerCorrect' in the class
    correct_option_element = item.find('li', class_='wpProQuiz_answerCorrect')
    correct_answer = int(correct_option_element['data-pos']) + 1 if correct_option_element else None

    # Extract explanation
    explanation_div = item.find('div', class_='wpProQuiz_response')
    explanation = ""
    if explanation_div:
        correct_response = explanation_div.find('div', class_='wpProQuiz_correct')
        incorrect_response = explanation_div.find('div', class_='wpProQuiz_incorrect')
        raw_explanation = correct_response.get_text(strip=True) if correct_response else incorrect_response.get_text(strip=True)
        
        # Clean up the explanation by removing "Correct" at the start
        explanation = re.sub(r'^Correct\s*', '', raw_explanation, flags=re.IGNORECASE)

    # Add the question data to the list with updated keys
    quiz_data = {
        "question_id": index,
        "question": question_text,
        "options": options,
        "correctAnswer": correct_answer,
        "explanation": explanation,
        "score": 1  # Set score to 1 for each question
    }
    all_quiz_data.append(quiz_data)

# Write all quiz data to JSON file
with open("all_quiz_data.json", "w") as file:
    json.dump(all_quiz_data, file, indent=4)

print("Data extracted and saved to all_quiz_data.json")
