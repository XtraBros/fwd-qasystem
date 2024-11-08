
function generateQuiz() {
    const container = document.getElementById('questionsContainer');
    quizData.forEach((item, index) => {
        const questionDiv = document.createElement('div');
        questionDiv.classList.add('question');

        const questionLabel = document.createElement('label');
        questionLabel.classList.add('question-label');
        questionLabel.innerText = item.question;
        questionDiv.appendChild(questionLabel);

        item.options.forEach((option, optionIndex) => {
            const optionLabel = document.createElement('label');
            const optionInput = document.createElement('input');
            optionInput.type = item.correctAnswer.length > 1 ? 'checkbox' : 'radio';
            optionInput.name = `question${index}`;
            optionInput.value = String.fromCharCode(65 + optionIndex); // A, B, C, D
            optionLabel.appendChild(optionInput);
            optionLabel.appendChild(document.createTextNode(option));
            questionDiv.appendChild(optionLabel);
            questionDiv.appendChild(document.createElement('br'));
        });

        container.appendChild(questionDiv);
    });
}

async function submitForm(event) {
    event.preventDefault();

    // Clear previous results
    clearPreviousResults();

    const model = document.getElementById('modelSelect').value;
    const questions = document.querySelectorAll('.question');
    let totalScore = 0;

    for (let i = 0; i < questions.length; i++) {
        const question = questions[i];
        const questionText = quizData[i].question;
        const options = question.querySelectorAll('input[type="radio"], input[type="checkbox"]');
        let selectedOptions = '';

        // Simulate the thinking process using setTimeout
        await new Promise(resolve => setTimeout(resolve, i * 500));

        options.forEach(option => {
            if (option.checked) {
                selectedOptions += option.value;
            }
        });

        // Simulate the thinking process using setTimeout
        await new Promise(resolve => setTimeout(resolve, i * 500));

        const response = await fetch('/answer', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                question: questionText,
                selectedOptions: selectedOptions,
                model: model // Add model to the request body
            })
        });

        const result = await response.json();
        console.log(`Recommended answer for "${questionText}": ${result.recommendedAnswer}`);

        // Select the recommended answer based on the returned answer
        const recommendedAnswer = result.recommendedAnswer;
        options.forEach(option => {
            if (recommendedAnswer.includes(option.value)) {
                option.checked = true;
            } else {
                option.checked = false;
            }
        });

        // Compare the recommended answer and the correct answer
        const correctAnswer = quizData[i].correctAnswer;
        const resultText = recommendedAnswer === correctAnswer ? 
            'AI answer: correct' : 
            `AI answer: wrong. Correct answer is: ${correctAnswer}`;

        // Output the result at the end of the question
        const lastOption = options[options.length - 1].parentElement;
        const resultElement = document.createElement('div');
        resultElement.style.marginTop = '10px';
        resultElement.style.color = recommendedAnswer === correctAnswer ? 'green' : 'red';
        resultElement.innerText = resultText;
        resultElement.classList.add('result-text');
        lastOption.appendChild(resultElement);

        // Calculate the total score
        if (recommendedAnswer === correctAnswer) {
            totalScore += quizData[i].score;
        }
    }

    // Output the total score
    const totalScoreElement = document.createElement('div');
    totalScoreElement.style.marginTop = '20px';
    totalScoreElement.style.fontWeight = 'bold';
    totalScoreElement.innerText = `Total score: ${totalScore} out of 10`;
    totalScoreElement.id = 'totalScore';
    document.body.appendChild(totalScoreElement);
}

function clearPreviousResults() {
    // Clear all selected options
    const options = document.querySelectorAll('input[type="radio"], input[type="checkbox"]');
    options.forEach(option => {
        option.checked = false;
    });

    // Clear previous comparison results
    const resultElements = document.querySelectorAll('.result-text');
    resultElements.forEach(element => {
        element.remove();
    });

    // Clear total score
    const totalScoreElement = document.getElementById('totalScore');
    if (totalScoreElement) {
        totalScoreElement.remove();
    }
}

document.getElementById('quizForm').addEventListener('submit', submitForm);
window.onload = generateQuiz;