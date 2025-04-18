// main.js - For dashboard interactivity

document.addEventListener('DOMContentLoaded', function() {
    // Example: Highlight table rows on click
    const rows = document.querySelectorAll('table tr');
    rows.forEach(row => {
        row.addEventListener('click', function() {
            rows.forEach(r => r.classList.remove('selected'));
            this.classList.add('selected');
        });
    });

    // Example: Simple toggle for cards (expand/collapse)
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('click', function() {
            this.classList.toggle('collapsed');
        });
    });

    // Example: Show alert for file upload (if present)
    const uploadInput = document.getElementById('file-upload');
    if (uploadInput) {
        uploadInput.addEventListener('change', function() {
            alert('File selected: ' + this.files[0].name);
        });
    }
});
