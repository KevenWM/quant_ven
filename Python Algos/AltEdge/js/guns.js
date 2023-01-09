document.addEventListener('DOMContentLoaded', () => {

    // Call the readCSV function with a URL to retrieve and display the CSV data
    readCSV('http://127.0.0.1:5500/AltEdge/data/gunsprice.csv');

    // Criando menu dropdown to select the car
    async function readCSV(url) {
        // Send a request to the URL to retrieve the CSV file
        const response = await fetch(url);
        const csv = await response.text();

        // Split the CSV data into an array of rows
        const rows = csv.split('\n');

        // Map over each row and split it into an array of cells, skipping the first row
        const data = rows.slice(1).map(row => row.split(';'));

        // Remove duplicate elements from the data array using the Set object
        const uniqueData = [...new Set(data.map(row => row[0]))];

        // Convert the uniqueData array into a dropdown menu
        var result = '<select>';
        for (var i = 0; i < uniqueData.length; i++) {
            result += '<option value="' + uniqueData[i] + '">' + uniqueData[i] + '</option>'; // Add an option element for each unique element
        }
        result += '</select>';

        // Display the dropdown menu on the HTML page
        document.getElementById('result2').innerHTML = result;
    }

    var car_name = "AGENCY ARMS LLC"

    function carregar_guns(car_name) {

        fetch('http://127.0.0.1:5500/AltEdge/data/gunsprice.csv')
            .then(response => response.text())
            .then(csv => {

                const rows = csv.split('\r')
                const firstRow = rows[0]; // Get the first row
                const datas = firstRow.split(';'); // Split the row into columns using a semicolon as the separator
                datas.shift()

                console.log(rows[1])

                const filteredRows = rows.filter(row => row.split(';')[0] === car_name);

                const series_data = filteredRows[0].split(';')
                series_data.shift()
                series_data.shift()

                for (let i = 0; i < series_data.length; i++) {
                    series_data[i] = parseFloat(series_data[i].replace(',', '.'));
                }
                //ANTIGO
                // .then(response => response.text())
                // .then(csvData => {
                //     const rows = csvData.split('\n');
                //     const data = rows.map(row => row.split(';'));
                //     return data;
                // })
                //
                // .then(data => data.map(row => row.map(cell => cell.replace('"', ''))))
                //
                //
                // .then(data => data.filter(row => row[1] === car_name))
                //
                //
                // .then(data => {
                //
                //
                //     const dates = data.map(row => row[0]);
                //
                //     list = data.map(row => {
                //
                //         const price = row[2].replace('.', '')
                //
                //         return {
                //             date: row[0],
                //             car: row[1],
                //             price: parseInt(price, 10)
                //         };
                //     });
                //ANTIGO


                Highcharts.chart('container2', {


                    title: {
                        text: 'Global Gun Prices',
                        align: 'left'
                    },

                    yAxis: {
                        title: {
                            text: 'Price'
                        }
                    },

                    xAxis: {
                        categories: datas
                    },

                    legend: {
                        layout: 'vertical',
                        align: 'right',
                        verticalAlign: 'middle'
                    },


                    series: [{
                        name: car_name,
                        data: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                    },
                    ],

                    responsive: {
                        rules: [{
                            condition: {
                                maxWidth: 500
                            },
                            chartOptions: {
                                legend: {
                                    layout: 'horizontal',
                                    align: 'center',
                                    verticalAlign: 'bottom'
                                }
                            }
                        }]
                    },

                    credits: {
                        enabled: false
                    },

                });
            })
    }

    carregar_guns(car_name)

    // Declare the car_name variable
    let xcar;

    // Get the select element
    const select = document.getElementById('result2');

    // Add an input event listener to the select element
    select.addEventListener('input', function () {
        // Get the value of the selected option
        xcar = this.value;
        var car_name = xcar;
        carregar_guns(car_name)


    });


})