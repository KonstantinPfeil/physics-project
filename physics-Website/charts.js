fetch("/api/data/")
    .then(res => {return res.json()})
    .then(data => drawChart(data["t"], data["s"], data["ps"]));

var myChart = null;

function drawChart(xs, ys, pys){
    if (myChart != null) myChart.destroy();

    let points = new Array(xs.length);
    for(let i = 0; i< points.length; i++){
        points[i] = {
            x: xs[i],
            y: ys[i]
        }
    }

    let predictions = new Array(xs.length);
    for(let i = 0; i<predictions.length; i++){
        predictions[i] = {
            x: xs[i],
            y: pys[i]
        }
    }

    const data = {
        datasets: [
            {
                label: 't-s',
                data: points,
                backgroundColor: 'rgb(255, 99, 132)',
                type: 'scatter',
                order: 2
            },
            {
                label: "prediction",
                data: predictions,
                backgroundColor: "rgb(0,122,255)",
                type: 'scatter',
                order: 1
            }
        ],

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

    myChart = new Chart(
        document.getElementById('chartTS'),
        config
    );
}

document.getElementById("fileupload").addEventListener("change",
        event => {
            const files = event.target.files
            const formdata = new FormData();
            formdata.append("file", files[0])
            fetch("/api/data/", {method: "Post", body: formdata})
                .then( res => {return res.json()})
                .then( res => {drawChart(res["t"], res["s"], res["ps"])})
        }
)