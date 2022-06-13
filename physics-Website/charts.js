fetch("http://localhost:8000/data/")
    .then(res => {return res.json()})
    .then(data => drawChart(data["times"], data["weg"]));

function drawChart(xs, ys){
    let points = new Array(xs.length)
    for(let i = 0; i< points.length; i++){
        points[i] = {
            x: xs[i],
            y: ys[i]
        }
    }

    const data = {
        datasets: [{
            label: 'Scatter Dataset',
            data: points,
            backgroundColor: 'rgb(255, 99, 132)'
        }],
    };

    const config = {
        type: 'scatter',
        data: data,
        options: {
            scales: {
                x: {
                    type: 'linear',
                    position: 'bottom'
                }
            }
        }
    };

    const myChart = new Chart(
        document.getElementById('chartTS'),
        config
    );
}
