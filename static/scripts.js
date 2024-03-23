// scripts.js

document.getElementById('translate-btn').addEventListener('click', function() {
    var text = document.getElementById('input-text').value;
    fetch('/translate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('output-text').innerText = data.translated_text;
    });
});
