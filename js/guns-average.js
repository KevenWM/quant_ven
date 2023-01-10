

function create_guns() {
    fetch('http://127.0.0.1:5500/AltEdge/data/guns-average.csv')
        .then(response => response.text())
        .then(csv => {

            const rows = csv.split('\r');
            const data2 = rows.map(row => row.split(';'));

            // Extract the categories and series data from the array
            var categoriess = data2.map(row => row[0]); // Second column
            var seriesData = data2.map(row => row[row.length - 1]); // Last column

            var cias = categoriess.shift();
            var date = seriesData.shift();


            for (var i = 0; i < seriesData.length; i++) {

                seriesData[i] = seriesData[i].replace(',', '.')
                seriesData[i] = parseFloat(seriesData[i]);
            }



            // Create the chart
            Highcharts.chart('guns-average', {
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'Guns price historical average',
                    align: 'left'
                },
                xAxis: {
                    categories: categoriess
                },
                yAxis: {

                },
                series: [{
                    name: 'Notas',
                    data: seriesData
                }],
                credits: {
                    enabled: false
                },

            });
        });
}

// When the page is ready, create the chart
$(document).ready(function () {

    create_guns();

});
