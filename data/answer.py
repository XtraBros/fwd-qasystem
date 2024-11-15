import json
import string

filename = "all_quiz_data.json" #change as required

def add_indices_to_options(quiz_data):
    # Alphabetical labels (A, B, C, D, ...)
    labels = string.ascii_uppercase
    
    # Add indexed options for each question
    for item in quiz_data:
        item["options"] = [f"{labels[i]}. {option}" for i, option in enumerate(item["options"])]

def update_correct_answers(correct_answers):
    # Load existing quiz data from the JSON file
    with open(filename, "r") as file:
        quiz_data = json.load(file)

    # Add indices to the options if not already done
    add_indices_to_options(quiz_data)

    # Ensure the correct_answers list matches the number of questions
    if len(correct_answers) != len(quiz_data):
        print("Error: The number of answers provided does not match the number of questions in the JSON file.")
        return

    # Convert numeric answers to letter indices
    labels = string.ascii_uppercase  # 'A', 'B', 'C', 'D', ...
    for i, correct_answer in enumerate(correct_answers):
        if 1 <= correct_answer <= len(quiz_data[i]["options"]):
            # Update correctAnswer with the corresponding letter
            quiz_data[i]["correctAnswer"] = labels[correct_answer - 1]
        else:
            print(f"Warning: Question {i + 1} has an invalid correct answer index.")

    # Save the updated quiz data back to the JSON file
    with open(filename, "w") as file:
        json.dump(quiz_data, file, indent=4)

    print("Options indexed and correct answers updated successfully in all_quiz_data.json")

# Example usage: Provide a list of correct answer indices (integers)
# Replace this list with the actual correct answers for each question
correct_answers_list = [1,3,3,4,3,1,3,3,1,2,3,3,4,1,1,2,4,3,4,4,3,4,3,4,3,4,4,3,4,2]# update based on questions.
update_correct_answers(correct_answers_list)
