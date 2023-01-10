document.addEventListener('DOMContentLoaded', () => {
    fetch('http://127.0.0.1:5500/AltEdge/data/other data/marcas_zerokm.csv')

        .then(response => response.text())
        .then(csvData => {
            const rows = csvData.split('\n');
            const data = rows.map(row => row.split(';'));

            let names = rows[0].split(';')


            let n1 = names[1]
            let n2 = names[2]
            let n3 = names[3]
            let n4 = names[4]

            let datas_px = []
            let n1_d = []
            let n2_d = []
            let n3_d = []
            let n4_d = []


            for (const row of rows) {
                let row2 = row.split(';')

                for (var i = 1; i < row2.length; i++) {

                    row2[i] = row2[i].replace('.', '')
                    row2[i] = parseFloat(row2[i]);
                }

                datas_px.push(row2[0])
                n1_d.push(row2[1])
                n2_d.push(row2[2])
                n3_d.push(row2[3])
                n4_d.push(row2[4])

            }


            datas_px.shift()
            n1_d.shift()
            n2_d.shift()
            n3_d.shift()
            n4_d.shift()


            console.log(datas_px)


            Highcharts.chart('camin-zero', {


                title: {
                    text: 'Truck Zero KM Brand Prices',
                    align: 'left'
                },

                yAxis: {
                    title: {
                        text: 'Price'
                    }
                },

                xAxis: {
                    categories: datas_px
                },

                legend: {
                    layout: 'vertical',
                    align: 'right',
                    verticalAlign: 'middle'
                },


                series: [{
                    name: n1,
                    data: n1_d,
                }, {
                    name: n2,
                    data: n2_d,
                }, {
                    name: n3,
                    data: n3_d,
                }, {
                    name: n4,
                    data: n4_d,
                },],

                credits: {
                    enabled: false
                },

            });

        });

    fetch('http://127.0.0.1:5500/AltEdge/data/other data/marcas_seminovo.csv')

        .then(response => response.text())
        .then(csvData => {
            const rows = csvData.split('\n');
            const data = rows.map(row => row.split(';'));

            let names = rows[0].split(';')


            let n1 = names[1]
            let n2 = names[2]
            let n3 = names[3]
            let n4 = names[4]

            let datas_px = []
            let n1_d = []
            let n2_d = []
            let n3_d = []
            let n4_d = []


            for (const row of rows) {
                let row2 = row.split(';')

                for (var i = 1; i < row2.length; i++) {

                    row2[i] = row2[i].replace('.', '')
                    row2[i] = parseFloat(row2[i]);
                }

                datas_px.push(row2[0])
                n1_d.push(row2[1])
                n2_d.push(row2[2])
                n3_d.push(row2[3])
                n4_d.push(row2[4])

            }


            datas_px.shift()
            n1_d.shift()
            n2_d.shift()
            n3_d.shift()
            n4_d.shift()


            console.log(datas_px)


            Highcharts.chart('camin-semi', {


                title: {
                    text: 'Used Truck Brand Prices',
                    align: 'left'
                },

                yAxis: {
                    title: {
                        text: 'Price'
                    }
                },

                xAxis: {
                    categories: datas_px
                },

                legend: {
                    layout: 'vertical',
                    align: 'right',
                    verticalAlign: 'middle'
                },


                series: [{
                    name: n1,
                    data: n1_d,
                }, {
                    name: n2,
                    data: n2_d,
                }, {
                    name: n3,
                    data: n3_d,
                }, {
                    name: n4,
                    data: n4_d,
                },],

                credits: {
                    enabled: false
                },

            });

        });

    fetch('http://127.0.0.1:5500/AltEdge/data/other data/caminhao.csv')

        .then(response => response.text())
        .then(csvData => {
            const rows = csvData.split('\n');
            const data = rows.map(row => row.split(';'));

            let names = rows[0].split(';')


            let n1 = names[1]
            let n2 = names[2]


            let datas_px = []
            let n1_d = []
            let n2_d = []



            for (const row of rows) {
                let row2 = row.split(';')

                for (var i = 1; i < row2.length; i++) {

                    row2[i] = row2[i].replace('.', '')
                    row2[i] = parseFloat(row2[i]);
                }

                datas_px.push(row2[0])
                n1_d.push(row2[1])
                n2_d.push(row2[2])


            }


            datas_px.shift()
            n1_d.shift()
            n2_d.shift()



            console.log(datas_px)


            Highcharts.chart('camin', {


                title: {
                    text: 'Total Truck Prices',
                    align: 'left'
                },

                yAxis: {
                    title: {
                        text: 'Price'
                    }
                },

                xAxis: {
                    categories: datas_px
                },

                legend: {
                    layout: 'vertical',
                    align: 'right',
                    verticalAlign: 'middle'
                },


                series: [{
                    name: n1,
                    data: n1_d,
                }, {
                    name: n2,
                    data: n2_d,
                },],

                credits: {
                    enabled: false
                },

            });

        });
})
