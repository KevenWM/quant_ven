

function createrm_varejo() {
    fetch('https://kevenwm.github.io/quant_ven/data/reclame aqui/varejo.csv')
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
            Highcharts.chart('containerm-varejo', {
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'Varejo Reclame Aqui - ' + date,
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

function createrm_bancos() {
    fetch('https://kevenwm.github.io/quant_ven/data/reclame aqui/bancos.csv')
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
            Highcharts.chart('containerm-bancos', {
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'Bancos Reclame Aqui - ' + date,
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

function createrm_drogarias() {
    fetch('https://kevenwm.github.io/quant_ven/data/reclame aqui/drogarias.csv')
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
            Highcharts.chart('containerm-drogarias', {
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'Drogarias Reclame Aqui - ' + date,
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
function createrm_locadoras() {
    fetch('https://kevenwm.github.io/quant_ven/data/reclame aqui/locadoras.csv')
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
            Highcharts.chart('containerm-locadoras', {
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'Locadoras Reclame Aqui - ' + date,
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
function createrm_restaurantes() {
    fetch('https://kevenwm.github.io/quant_ven/data/reclame aqui/restaurantes.csv')
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
            Highcharts.chart('containerm-restaurantes', {
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'Restaurantes Reclame Aqui - ' + date,
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
function createrm_vestuario() {
    fetch('https://kevenwm.github.io/quant_ven/data/reclame aqui/vestuario.csv')
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
            Highcharts.chart('containerm-vestuario', {
                chart: {
                    type: 'column'
                },
                title: {
                    text: 'Vestuário Reclame Aqui - ' + date,
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

    createrm_varejo();
    createrm_bancos();
    createrm_drogarias();
    createrm_locadoras();
    createrm_restaurantes();
    createrm_vestuario();
});
