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

// Check answers only
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

document.addEventListener("DOMContentLoaded", renderQuestions);