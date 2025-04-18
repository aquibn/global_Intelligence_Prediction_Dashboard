// static/js/chart.js

// This function renders a bar chart for vulnerabilities by environment
function renderEnvironmentBarChart(ctxId, labels, data) {
    const ctx = document.getElementById(ctxId).getContext('2d');
    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels, // e.g., ['Windows 10', 'Linux', 'Apache', ...]
            datasets: [{
                label: 'Number of Vulnerabilities',
                data: data,    // e.g., [1102, 18815, 2182, ...]
                backgroundColor: [
                    'rgba(54, 162, 235, 0.7)',
                    'rgba(255, 99, 132, 0.7)',
                    'rgba(255, 206, 86, 0.7)',
                    'rgba(75, 192, 192, 0.7)',
                    'rgba(153, 102, 255, 0.7)',
                    'rgba(255, 159, 64, 0.7)',
                    'rgba(100, 255, 218, 0.7)',
                    'rgba(255, 99, 71, 0.7)'
                ],
                borderColor: [
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 99, 132, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)',
                    'rgba(100, 255, 218, 1)',
                    'rgba(255, 99, 71, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: false },
                title: { display: true, text: 'Vulnerabilities by Environment' }
            },
            scales: {
                y: { beginAtZero: true }
            }
        }
    });
}

// This function renders a pie chart for attack vectors
function renderAttackVectorPieChart(ctxId, labels, data) {
    const ctx = document.getElementById(ctxId).getContext('2d');
    new Chart(ctx, {
        type: 'pie',
        data: {
            labels: labels, // e.g., ['Physical', 'Network', 'Adjacent', 'Local']
            datasets: [{
                label: 'Attack Vectors',
                data: data,    // e.g., [74252, 55180, 32141, 37395]
                backgroundColor: [
                    'rgba(255, 99, 132, 0.7)',
                    'rgba(54, 162, 235, 0.7)',
                    'rgba(255, 206, 86, 0.7)',
                    'rgba(75, 192, 192, 0.7)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { position: 'bottom' },
                title: { display: true, text: 'Attack Vectors Distribution' }
            }
        }
    });
}

// Example usage (replace with your actual data passed from Flask/Jinja2)
document.addEventListener('DOMContentLoaded', function() {
    // Example data (replace with Jinja2 variables in your template)
    // let envLabels = {{ env_labels|tojson }};
    // let envData = {{ env_data|tojson }};
    // let vectorLabels = {{ vector_labels|tojson }};
    // let vectorData = {{ vector_data|tojson }};

    // For demonstration, use hardcoded data:
    let envLabels = ['Windows 10', 'Linux', 'Apache', 'Samba', 'Apple', 'SQL', 'Post Gres'];
    let envData = [1102, 18815, 2182, 14864, 7222, 9288, 255];

    let vectorLabels = ['Physical', 'Network', 'Adjacent', 'Local'];
    let vectorData = [74252, 55180, 32141, 37395];

    // Render charts if canvas elements exist
    if (document.getElementById('envBarChart')) {
        renderEnvironmentBarChart('envBarChart', envLabels, envData);
    }
    if (document.getElementById('vectorPieChart')) {
        renderAttackVectorPieChart('vectorPieChart', vectorLabels, vectorData);
    }
});
