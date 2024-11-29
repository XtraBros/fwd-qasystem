// Code to generate HTML for open ended questions from the spring 2024 exam sets.
function renderQuestions() {
    const container = document.getElementById("questions-container");
    container.innerHTML = ''; // Clear any existing content

    questionData.forEach((q, index) => {
        const questionDiv = document.createElement("div");
        questionDiv.classList.add("question");

        // Set the question_id attribute
        questionDiv.setAttribute("data-question-id", q.question_id);

        // Format and number the question text
        const formattedQuestionText = `${index + 1}. ${q.question.replace(/\n/g, '<br>')}`;
        
        const label = document.createElement("label");
        label.classList.add("question-label");
        label.innerHTML = formattedQuestionText; // Use innerHTML to keep formatting
        questionDiv.appendChild(label);

        // Add score display
        const scoreDiv = document.createElement("div");
        scoreDiv.classList.add("score");
        scoreDiv.innerText = `Score: ${q.score}`;
        questionDiv.appendChild(scoreDiv);

        // Add data (if available)
        if (q.data && q.data.length > 0) {
            const dataContainer = document.createElement("div");
            dataContainer.classList.add("question-data-table");

            q.data.forEach((dataRow) => {
                const dataRowDiv = document.createElement("div");
                dataRowDiv.classList.add("data-row");
                dataRowDiv.innerText = dataRow;
                dataContainer.appendChild(dataRowDiv);
            });

            questionDiv.appendChild(dataContainer);
        }

        // Add an answer input box
        const answerContainer = document.createElement("div");
        answerContainer.classList.add("answer-container");

        const answerLabel = document.createElement("label");
        answerLabel.setAttribute("for", `answer${index}`);
        answerLabel.innerText = "Your Answer:";

        const answerInput = document.createElement("textarea");
        answerInput.id = `answer${index}`;
        answerInput.name = `answer${index}`;
        answerInput.rows = 4;
        answerInput.cols = 50;
        answerInput.placeholder = "Type your answer here...";

        answerContainer.appendChild(answerLabel);
        answerContainer.appendChild(answerInput);
        questionDiv.appendChild(answerContainer);

        // Append the question block to the container
        container.appendChild(questionDiv);
    });
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