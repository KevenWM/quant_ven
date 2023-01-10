
document.addEventListener('DOMContentLoaded', () => {

    let list;
    let car_name = 'Volkswagen Nivus'

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
            // Inside the then callback, assign the list variable to the array of objects
            list = data.map(row => {

                const price = row[2].replace(/,/g, '').replace(/\./g, '');

                return {
                    date: row[0],
                    car: row[1],
                    price: parseInt(price, 10)
                };
            });

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
                    accessibility: {
                        rangeDescription: 'Range: 2010 to 2020'
                    }
                },

                legend: {
                    layout: 'vertical',
                    align: 'right',
                    verticalAlign: 'middle'
                },

                plotOptions: {
                    series: {
                        label: {
                            connectorAllowed: false
                        },
                        pointStart: 2010
                    }
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
                }

            });
        })

})

