document.addEventListener('DOMContentLoaded', () => {
    // Call the readCSV function with a URL to retrieve and display the CSV data
    readCSV('http://127.0.0.1:5500/AltEdge/data/Reclame11.csv');

    // Criando menu dropdown to select the car
    async function readCSV(url) {
        // Send a request to the URL to retrieve the CSV file
        const response = await fetch(url);
        const csv = await response.text();

        // Split the CSV data into an array of rows
        const rows = csv.split('\n');

        // Initialize an array to hold the column data
        const data = [];

        // Iterate over each row, and split it into an array of cells
        for (const row of rows) {
            const cells = row.split(';');

            // Iterate over each cell and add its value to the appropriate column in the data array
            for (let i = 0; i < cells.length; i++) {
                if (!data[i]) data[i] = [];  // Initialize the column array if it doesn't already exist
                data[i].push(cells[i]);
            }
        }

        // Remove duplicate elements from each column using the Set object
        const uniqueData = data.map(column => [...new Set(column)]);
        uniqueData[1].shift()


        // Convert the uniqueData array into a dropdown menu
        var result = '<select>';
        for (var i = 0; i < uniqueData[1].length; i++) {
            result += '<option value="' + uniqueData[1][i] + '">' + uniqueData[1][i] + '</option>'; // Add an option element for each unique element in the first column
        }
        result += '</select>';

        // Display the dropdown menu on the HTML page
        document.getElementById('result_reclame').innerHTML = result;
    }

    var car_name = "Centauro- Loja teste"

    // Get a reference to the select element
    function createChart_hist(car_name) {
        fetch('http://127.0.0.1:5500/AltEdge/data/Reclame11.csv')
            .then(response => response.text())
            .then(csv => {

                const rows = csv.split('\r')
                const firstRow = rows[0]; // Get the first row
                const datas = firstRow.split(';'); // Split the row into columns using a semicolon as the separator
                datas.shift()
                datas.shift()



                const filteredRows = rows.filter(row => row.split(';')[1] === car_name);

                const series_data = filteredRows[0].split(';')
                series_data.shift()
                series_data.shift()

                for (let i = 0; i < series_data.length; i++) {
                    series_data[i] = parseFloat(series_data[i]);
                }

                // Create the chart
                Highcharts.chart('container5', {
                    chart: {
                        type: 'column',
                    },
                    title: {
                        text: 'Notas Reclame Aqui - Histórico',
                        align: 'left'
                    },
                    xAxis: {
                        categories: datas
                    },
                    yAxis: {
                        min: 0,
                        title: {
                            text: 'Notas'
                        }
                    },
                    series: [{
                        name: 'Datas',
                        data: series_data
                    }],
                    credits: {
                        enabled: false
                    },

                });
            });

    }
    // Use fetch to read the CSV file

    createChart_hist(car_name)

    let xcar;

    const select = document.querySelector('#result_reclame');

    select.addEventListener('input', function () {

        xcar = this.value;
        var car_name = xcar;

        let list;

        createChart_hist(car_name)


    },
    )


})

