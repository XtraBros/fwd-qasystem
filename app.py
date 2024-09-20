from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/answer', methods=['POST'])
def answer():
    data = request.get_json()
    question = data.get('question')
    selected_options = data.get('selectedOptions')
    
    recommended_answer = random.choice(["A", "B", "C", "D"])
    
    return jsonify({
        'question': question,
        'selectedOptions': selected_options,
        'recommendedAnswer': recommended_answer
    })

# Subpage 1
@app.route('/module_1', methods=['GET', 'POST'])
def subpage1():
    if request.method == 'POST':
        answers = request.form.to_dict()
        return jsonify(answers)
    return render_template('module_1.html')

# Subpage 2
@app.route('/module_2', methods=['GET', 'POST'])
def subpage2():
    if request.method == 'POST':
        answers = request.form.to_dict()
        return jsonify(answers)
    return render_template('module_2.html')

# Subpage 3
@app.route('/module_3', methods=['GET', 'POST'])
def subpage3():
    if request.method == 'POST':
        answers = request.form.to_dict()
        return jsonify(answers)
    return render_template('module_3.html')

if __name__ == '__main__':
    app.run(debug=True)