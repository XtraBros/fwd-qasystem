// Load questions from questionsData and render them
function renderQuestions() {
    const container = document.getElementById("questions-container");
    container.innerHTML = ''; // Clear any existing content

    questionsData.forEach((q, index) => {
        const questionDiv = document.createElement("div");
        questionDiv.classList.add("question");
        
        // Set the question_id attribute
        questionDiv.setAttribute("data-question-id", q.question_id);

        // Format and number the question text
        const formattedQuestionText = `${index + 1}. ${formatQuestionText(q.question)}`;
        
        const label = document.createElement("label");
        label.classList.add("question-label");
        label.innerHTML = formattedQuestionText; // Use innerHTML to keep formatting
        questionDiv.appendChild(label);

        q.options.forEach((option, i) => {
            const optionDiv = document.createElement("div");
            optionDiv.classList.add("option");

            const input = document.createElement("input");
            input.type = "radio";
            input.name = `question${index}`;
            input.id = `q${index}option${i}`;
            input.value = option[0];

            const optionLabel = document.createElement("label");
            optionLabel.setAttribute("for", `q${index}option${i}`);
            optionLabel.innerText = option;

            optionDiv.appendChild(input);
            optionDiv.appendChild(optionLabel);
            questionDiv.appendChild(optionDiv);
        });

        container.appendChild(questionDiv);
    });
}

// Helper function to format question text with line breaks or bullet points
function formatQuestionText(text) {
    // Split the question into parts based on indicators like "I.", "II.", etc.
    // You can also add more patterns here as needed.
    const formattedText = text.replace(/(I\.|II\.|III\.|IV\.|V\.)/g, '<br>$1');
    return formattedText;
}

// Check answers via endpoint.
async function submitForm(event) {
    event.preventDefault();

    const questions = document.querySelectorAll('.question');
    let totalScore = 0;
    let maxScore = 0;
    for (let i = 0; i < questions.length; i++) {
        const question = questions[i];
        const questionId = question.getAttribute("data-question-id"); // Get question_id from attribute
        const options = question.querySelectorAll('input[type="radio"], input[type="checkbox"]');
        let selectedOptions = '';

        options.forEach(option => {
            if (option.checked) {
                selectedOptions += option.value;
            }
        });

        // Simulate a delay for processing each question to appear sequential
        await new Promise(resolve => setTimeout(resolve, i * 100));

        const response = await fetch('/answer', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                question_id: questionId,
                selectedOptions: selectedOptions
            })
        });

        const result = await response.json();
        console.log(`Recommended answer for question ID "${questionId}": ${result.recommendedAnswer}`);

        // Check the radio or checkbox based on the returned answer
        const recommendedAnswer = result.recommendedAnswer;
        options.forEach(option => {
            option.checked = recommendedAnswer.includes(option.value);
        });

        // Retrieve the correct answer and score using question_id
        const questionData = questionsData.find(q => q.question_id == questionId);
        const correctAnswer = questionData ? questionData.correctAnswer : '';
        const questionScore = questionData ? questionData.score : 0;

        // Display whether the AI answer is correct or not
        const resultText = recommendedAnswer === correctAnswer ? 
            'AI answer: correct' : 
            `AI answer: wrong. Correct answer is: ${correctAnswer}`;

        // Remove any existing result message before adding the new one
        let resultElement = question.querySelector('.result-message');
        if (!resultElement) {
            resultElement = document.createElement('div');
            resultElement.classList.add('result-message');
            resultElement.style.marginTop = '10px';
            question.appendChild(resultElement);
        }
        resultElement.style.color = recommendedAnswer === correctAnswer ? 'green' : 'red';
        resultElement.innerText = resultText;

        // Add to the total score if the AI answer is correct
        if (recommendedAnswer === correctAnswer) {
            totalScore += questionScore;
        }
        maxScore += questionScore;
    }

    // Output the total score, replacing any previous score display
    let totalScoreElement = document.getElementById('total-score');
    if (!totalScoreElement) {
        totalScoreElement = document.createElement('div');
        totalScoreElement.id = 'total-score';
        totalScoreElement.style.marginTop = '20px';
        totalScoreElement.style.fontWeight = 'bold';
        document.body.appendChild(totalScoreElement);
    }
    totalScoreElement.innerText = `Total score: ${totalScore} out of ${maxScore}`;
}

document.addEventListener("DOMContentLoaded", renderQuestions);