
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import pandas as pd
import ast
import json
import numpy as np

######################### Loading Config and Templates #########################
app = Flask(__name__)

CONFIG_FILE = 'config.json'

with open(CONFIG_FILE, 'r') as file:
    config = json.load(file)

client = OpenAI(api_key=config["OPENAI_API_KEY"])
model_name = config['GPT_MODEL']

# load local data files to supplement GPT #
# example
# data = pd.read_csv("questions_and_answers.csv")
data = None

######################### End points #########################
@app.route('/')
def home():
    return render_template('index.html')

# Solve User Query
@app.route('/solve', methods=['POST'])
def solve_question():
    payload = request.get_json()
    question = payload.get('question', '')

    if not question:
        return jsonify({'error': 'No question provided'}), 400

    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": f"""You task is to answer quiz questions about insurance policies, and give
                 an answer that is as accurate and correct as possible. You only need to reply with the answer to the question.
                Here is some data to help you: {str(data)}"""},
                {"role": "user", "content": question}
            ],
            temperature=0,
        )
        message = response.choices[0].message.content.strip()
        print(message)
        return jsonify({'message': message})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)