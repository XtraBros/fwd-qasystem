from flask import Blueprint, request, jsonify
import random

api = Blueprint('api', __name__)

@api.route('/answer', methods=['POST'])
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