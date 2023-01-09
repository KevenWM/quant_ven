document.addEventListener('DOMContentLoaded', () => {

    // Call the readCSV function with a URL to retrieve and display the CSV data
    readCSV('http://127.0.0.1:5500/Scrapping Locadoras/carros_movida_0km.csv');

    // Criando menu dropdown to select the car
    async function readCSV(url) {
        // Send a request to the URL to retrieve the CSV file
        const response = await fetch(url);
        const csv = await response.text();

        // Split the CSV data into an array of rows
        const rows = csv.split('\n');

        // Map over each row and split it into an array of cells, skipping the first row
        const data = rows.slice(1).map(row => row.split(','));

        // Remove duplicate elements from the data array using the Set object
        const uniqueData = [...new Set(data.map(row => row[1]))];

        // Convert the uniqueData array into a dropdown menu
        var result = '<select>';
        for (var i = 0; i < uniqueData.length; i++) {
            result += '<option value="' + uniqueData[i] + '">' + uniqueData[i] + '</option>'; // Add an option element for each unique element
        }
        result += '</select>';

        // Display the dropdown menu on the HTML page
        document.getElementById('result').innerHTML = result;
    }

    // ### -----------------------------------------------------------------------------------------------------###

    var car_name = "Chevrolet S10"

    function carrega_dados(car_name) {


        let list;


        fetch('http://127.0.0.1:5500/Scrapping Locadoras/carros_movida_0km.csv')


            // Parse the CSV data into a JavaScript array
            .then(response => response.text())
            .then(csvData => {
                const rows = csvData.split('\n');
                const data = rows.map(row => row.split(','));
                return data;
            })

            // Test for and remove a character from each cell
            .then(data => data.map(row => row.map(cell => cell.replace('"', ''))))

            // Filter the data to only include the rows with the desired car name
            .then(data => data.filter(row => row[1] === car_name))

            // Transform the data into an array of objects
            .then(data => {


                const dates = data.map(row => row[0]);

                // Inside the then callback, assign the list variable to the array of objects
                list = data.map(row => {

                    const price = row[2].replace(/,/g, '').replace(/\./g, '');

                    return {
                        date: row[0],
                        car: row[1],
                        price: parseInt(price, 10)
                    };
                });

                // --> GERA O GRÁFICO

                Highcharts.chart('container', {


                    title: {
                        text: 'Movida Rental Cars Prices',
                        align: 'left'
                    },

                    yAxis: {
                        title: {
                            text: 'Price'
                        }
                    },

                    xAxis: {
                        categories: dates
                    },

                    legend: {
                        layout: 'vertical',
                        align: 'right',
                        verticalAlign: 'middle'
                    },


                    series: [{
                        name: car_name,
                        data: list.map(item => item.price)
                    }],

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

    carrega_dados(car_name)

    // Declare the car_name variable
    let xcar;

    // Get the select element
    const select = document.getElementById('result');

    // Add an input event listener to the select element
    select.addEventListener('input', function () {
        // Get the value of the selected option
        xcar = this.value;
        var car_name = xcar;

        carrega_dados(car_name)


    });

})