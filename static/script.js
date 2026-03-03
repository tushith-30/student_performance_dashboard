fetch("/analytics")
.then(response => response.json())
.then(data => {

    document.getElementById("average").innerText = data.average;
    document.getElementById("topper").innerText = data.topper;
    document.getElementById("pass").innerText = data.pass_percentage + "%";

    const ctx = document.getElementById('subjectChart').getContext('2d');

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: Object.keys(data.subject_avg),
            datasets: [{
                label: 'Average Marks',
                data: Object.values(data.subject_avg)
            }]
        }
    });
});