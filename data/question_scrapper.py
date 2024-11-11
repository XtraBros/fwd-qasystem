import requests
from bs4 import BeautifulSoup
import json

# URL of the page with quiz questions
url = "https://cmfasexam.com/res-5-free-practice-test/"

# Send a request to the URL
response = requests.get(url)
# Ensure the request was successful
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
    # Extract explanation
    explanation_div = item.find('div', class_='wpProQuiz_response')
    explanation = ""
    if explanation_div:
        correct_response = explanation_div.find('div', class_='wpProQuiz_correct')
        incorrect_response = explanation_div.find('div', class_='wpProQuiz_incorrect')
        # Use the explanation text from correct or incorrect response as needed
        explanation = correct_response.get_text(strip=True) if correct_response else incorrect_response.get_text(strip=True)

    # Add the question data to the list
    quiz_data = {
        "question_id": index,  # Adding question index
        "question": question_text,
        "options": options,
        "correct_option": correct_option,  # Record correct option by data-pos number
        "explanation": explanation
    }
    all_quiz_data.append(quiz_data)

# Write all quiz data to JSON file
with open("all_quiz_data.json", "w") as file:
    json.dump(all_quiz_data, file, indent=4)

print("Data extracted and saved to all_quiz_data.json")
