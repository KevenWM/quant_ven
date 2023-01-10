
// Use fetch to read the CSV file
function createChart_gd() {
    fetch('http://127.0.0.1:5500/AltEdge/data/glassdoor/glassdor.csv')
        .then(response => response.text())
        .then(csv => {

            const rows = csv.split('\r');
            const data2 = rows.map(row => row.split(';'));

            // Extract the categories and series data from the array
            var categoriess = data2.map(row => row[1]); // Second column
            var seriesData = data2.map(row => row[row.length - 1]); // Last column

            var cias = categoriess.shift();
            var date = seriesData.shift();


            for (var i = 0; i < seriesData.length; i++) {

                seriesData[i] = seriesData[i].replace(',', '.')
                seriesData[i] = parseFloat(seriesData[i]);
            }



            // Create the chart
            Highcharts.chart('container-gd', {
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'Notas Glassdoor - ' + date,
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

function createChart_financial() {
    fetch('http://127.0.0.1:5500/AltEdge/data/glassdoor/Setor Financeiro.csv')
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
            Highcharts.chart('container-financial', {
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'Financial Sector Glassdoor - ' + date,
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

function createChart_varejo() {
    fetch('http://127.0.0.1:5500/AltEdge/data/glassdoor/varejo.csv')
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
            Highcharts.chart('container-varejo', {
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'Financial Sector Glassdoor - ' + date,
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

function createChart_instagram() {
    fetch('http://127.0.0.1:5500/AltEdge/data/Instagram 2.csv')
        .then(response => response.text())
        .then(csv => {

            const rows = csv.split('\r');
            const data2 = rows.map(row => row.split(';'));

            // Extract the categories and series data from the array
            var categoriess = data2.map(row => row[1]); // Second column
            var seriesData = data2.map(row => row[row.length - 1]); // Last column

            var cias = categoriess.shift();
            var date = seriesData.shift();


            for (var i = 0; i < seriesData.length; i++) {

                seriesData[i] = seriesData[i].replace(',', '.')
                seriesData[i] = parseFloat(seriesData[i]);
            }



            // Create the chart
            Highcharts.chart('container-instagram', {
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'Banks Instagram Followers - ' + date,
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
    createChart_gd();
    createChart_financial();
    createChart_varejo();
    createChart_instagram();
});
