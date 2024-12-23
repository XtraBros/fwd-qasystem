from flask import Blueprint, render_template, request, jsonify

pages = Blueprint('pages', __name__)

# Homepage
@pages.route('/')
def home():
    return render_template('home.html')

# Subpage 1
@pages.route('/module_1', methods=['GET', 'POST'])
def subpage1():
    if request.method == 'POST':
        answers = request.form.to_dict()
        return jsonify(answers)
    return render_template('module_1.html')

# Subpage 2
@pages.route('/module_2', methods=['GET', 'POST'])
def subpage2():
    if request.method == 'POST':
        answers = request.form.to_dict()
        return jsonify(answers)
    return render_template('module_2.html')

# Subpage 3
@pages.route('/module_3', methods=['GET', 'POST'])
def subpage3():
    if request.method == 'POST':
        answers = request.form.to_dict()
        return jsonify(answers)
    return render_template('module_3.html')

# HK Subpage 1
@pages.route('/hk_module_1', methods=['GET', 'POST'])
def hksubpage1():
    if request.method == 'POST':
        answers = request.form.to_dict()
        return jsonify(answers)
    return render_template('hk_module_1.html')

# HK Subpage 2
@pages.route('/hk_module_2', methods=['GET', 'POST'])
def hksubpage2():
    if request.method == 'POST':
        answers = request.form.to_dict()
        return jsonify(answers)
    return render_template('hk_module_2.html')

# HK Subpage 3
@pages.route('/hk_module_3', methods=['GET', 'POST'])
def hksubpage3():
    if request.method == 'POST':
        answers = request.form.to_dict()
        return jsonify(answers)
    return render_template('hk_module_3.html')

# Actuary exam
@pages.route('/actuary', methods=['GET', 'POST'])
def actuary():
    if request.method == 'POST':
        answers = request.form.to_dict()
        return jsonify(answers)
    return render_template('actuary.html')

# experimental page
@pages.route('/test', methods=['GET', 'POST'])
def test_page():
    if request.method == 'POST':
        answers = request.form.to_dict()
        return jsonify(answers)
    return render_template('test.html')