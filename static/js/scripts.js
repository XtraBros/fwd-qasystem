// Load questions from questionsData and render them
function renderQuestions() {
    const container = document.getElementById("questions-container");
    questionsData.forEach((q, index) => {
        const questionDiv = document.createElement("div");
        questionDiv.classList.add("question");

        const label = document.createElement("label");
        label.classList.add("question-label");
        label.innerText = q.question;
        questionDiv.appendChild(label);

        q.options.forEach((option, i) => {
            const optionDiv = document.createElement("div");
            optionDiv.classList.add("option");

            const input = document.createElement("input");
            input.type = q.type;
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

// Check answers only from data
async function submitForm(event) {
    event.preventDefault();

    let totalScore = 0;

    questionsData.forEach((q, index) => {
        const selectedOptions = Array.from(document.querySelectorAll(`[name="question${index}"]:checked`))
            .map(opt => opt.value)
            .join("");

        const resultDiv = document.createElement("div");
        resultDiv.style.marginTop = "10px";

        if (selectedOptions === q.correctAnswer) {
            resultDiv.style.color = "green";
            resultDiv.innerText = "Correct!";
            totalScore += q.score;
        } else {
            resultDiv.style.color = "red";
            resultDiv.innerText = `Incorrect. Correct answer: ${q.correctAnswer}`;
        }

        document.querySelectorAll(".question")[index].appendChild(resultDiv);
    });

    const scoreDisplay = document.createElement("div");
    scoreDisplay.innerText = `Total Score: ${totalScore}`;
    scoreDisplay.style.fontWeight = "bold";
    document.body.appendChild(scoreDisplay);
}

// Check answers via endpoint.
// async function submitForm(event) {
//     event.preventDefault();

//     const questions = document.querySelectorAll('.question');
//     let totalScore = 0;

//     for (let i = 0; i < questions.length; i++) {
//         const question = questions[i];
//         const questionText = question.querySelector('.question-label').innerText;
//         const options = question.querySelectorAll('input[type="radio"], input[type="checkbox"]');
//         let selectedOptions = '';

//         options.forEach(option => {
//             if (option.checked) {
//                 selectedOptions += option.value;
//             }
//         });

//         // Use setTimeout to simulate the thinking process
//         await new Promise(resolve => setTimeout(resolve, i * 500));

//         const response = await fetch('/answer', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify({
//                 question: questionText,
//                 selectedOptions: selectedOptions
//             })
//         });

//         const result = await response.json();
//         console.log(`Recommended answer for "${questionText}": ${result.recommendedAnswer}`);

//         // Check the raido and box based on the returned answer
//         const recommendedAnswer = result.recommendedAnswer;
//         options.forEach(option => {
//             if (recommendedAnswer.includes(option.value)) {
//                 option.checked = true;
//             } else {
//                 option.checked = false;
//             }
//         });
//         // Compare the recommended answer and the correct answer
//         const correctAnswer = correctAnswers[questionText];
//         const resultText = recommendedAnswer === correctAnswer ? 
//             'AI answer: correct' : 
//             `AI answer: wrong. Correct answer is: ${correctAnswer}`;

//         // Output the result at the end of the question
//         const lastOption = options[options.length - 1].parentElement;
//         const resultElement = document.createElement('div');
//         resultElement.style.marginTop = '10px';
//         resultElement.style.color = recommendedAnswer === correctAnswer ? 'green' : 'red';
//         resultElement.innerText = resultText;
//         lastOption.appendChild(resultElement);

//         // Calculate the total score
//         if (recommendedAnswer === correctAnswer) {
//             totalScore += questionScores[questionText];
//         }
//     }
    
//     // Output the total score
//     const totalScoreElement = document.createElement('div');
//     totalScoreElement.style.marginTop = '20px';
//     totalScoreElement.style.fontWeight = 'bold';
//     totalScoreElement.innerText = `Total score: ${totalScore} out of 100`;
//     document.body.appendChild(totalScoreElement);
// }

document.addEventListener("DOMContentLoaded", renderQuestions);