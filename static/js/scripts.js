document.getElementById('quiz-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const question = document.getElementById('question-input').value;
    const responseContainer = document.getElementById('response');

    responseContainer.textContent = 'Processing...';

    try {
        const response = await fetch('/solve', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question }),
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        responseContainer.textContent = data.message || 'No answer received';
    } catch (error) {
        responseContainer.textContent = 'An error occurred. Please try again.';
        console.error('Error:', error);
    }
});
