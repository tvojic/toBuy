document.addEventListener('DOMContentLoaded', function () {
    // Pie Chart
    var pieCtx = document.getElementById('pieChart').getContext('2d');
    var pieChart = new Chart(pieCtx, {
        type: 'pie',
        data: {
            labels: {{ pie_labels | tojson }},
            datasets: [{
                label: 'Products To Buy',
                data: {{ pie_data | tojson }},
                backgroundColor: {{ pie_colors | tojson }}
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });

    // Line Chart
    var lineCtx = document.getElementById('lineChart').getContext('2d');
    var lineChart = new Chart(lineCtx, {
        type: 'line',
        data: {
            labels: {{ line_labels | tojson }},
            datasets: [{
                label: 'Products Added Over Time',
                data: {{ line_data | tojson }},
                fill: false,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Date'
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Number of Products'
                    },
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
});
