
function trendrent() {
    fetch('https://kevenwm.github.io/quant_ven/Python Algos/AltEdge/data/gt-rent-a-car.csv')

        .then(response => response.text())
        .then(csvData => {
            const rows = csvData.split('\n');

            let names = rows[0].split(';')


            let n1 = names[1]
            let n2 = names[2]
            let n3 = names[3]



            let datas_px = []
            let n1_d2 = []
            let n2_d2 = []
            let n3_d2 = []



            for (const row of rows) {
                let row2 = row.split(';')

                for (var i = 1; i < row2.length; i++) {

                    row2[i] = row2[i].replace('.', '')
                    row2[i] = parseFloat(row2[i]);
                }

                datas_px.push(row2[0])
                n1_d2.push(row2[1])
                n2_d2.push(row2[2])
                n3_d2.push(row2[3])

            }


            datas_px.shift()
            n1_d2.shift()
            n2_d2.shift()
            n3_d2.shift()



            Highcharts.chart('gtrent', {


                title: {
                    text: 'Rent a Car Interest',
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
                    data: n1_d2,
                }, {
                    name: n2,
                    data: n2_d2,
                }, {
                    name: n3,
                    data: n3_d2,
                },],

                credits: {
                    enabled: false
                },

            });


        });

}

function trendjoalherias() {
    fetch('https://kevenwm.github.io/quant_ven/Python Algos/AltEdge/data/Joalherias.csv')

        .then(response => response.text())
        .then(csvData => {
            const rows = csvData.split('\n');

            let names = rows[0].split(';')


            let n1 = names[1]
            let n2 = names[2]
            let n3 = names[3]



            let datas_px = []
            let n1_d2 = []
            let n2_d2 = []
            let n3_d2 = []



            for (const row of rows) {
                let row2 = row.split(';')

                for (var i = 1; i < row2.length; i++) {

                    row2[i] = row2[i].replace('.', '')
                    row2[i] = parseFloat(row2[i]);
                }

                datas_px.push(row2[0])
                n1_d2.push(row2[1])
                n2_d2.push(row2[2])
                n3_d2.push(row2[3])

            }


            datas_px.shift()
            n1_d2.shift()
            n2_d2.shift()
            n3_d2.shift()



            Highcharts.chart('gtjewels', {


                title: {
                    text: 'Jewelry brand Interest',
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
                    data: n1_d2,
                }, {
                    name: n2,
                    data: n2_d2,
                }, {
                    name: n3,
                    data: n3_d2,
                },],

                credits: {
                    enabled: false
                },

            });


        });
}

function trendsocial() {
    fetch('https://kevenwm.github.io/quant_ven/Python Algos/AltEdge/data/Redes Sociais.csv')

        .then(response => response.text())
        .then(csvData => {
            const rows = csvData.split('\n');

            let names = rows[0].split(';')


            let n1 = names[1]
            let n2 = names[2]
            let n3 = names[3]
            let n4 = names[4]



            let datas_px = []
            let n1_d2 = []
            let n2_d2 = []
            let n3_d2 = []
            let n4_d2 = []



            for (const row of rows) {
                let row2 = row.split(';')

                for (var i = 1; i < row2.length; i++) {

                    row2[i] = row2[i].replace('.', '')
                    row2[i] = parseFloat(row2[i]);
                }

                datas_px.push(row2[0])
                n1_d2.push(row2[1])
                n2_d2.push(row2[2])
                n3_d2.push(row2[3])
                n4_d2.push(row2[4])

            }


            datas_px.shift()
            n1_d2.shift()
            n2_d2.shift()
            n3_d2.shift()
            n4_d2.shift()



            Highcharts.chart('gtsocial', {


                title: {
                    text: 'Social Media Interest',
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
                    data: n1_d2,
                }, {
                    name: n2,
                    data: n2_d2,
                }, {
                    name: n3,
                    data: n3_d2,
                }, {
                    name: n4,
                    data: n4_d2,
                },],

                credits: {
                    enabled: false
                },

            });


        });
}

function trendmoda() {
    fetch('https://kevenwm.github.io/quant_ven/Python Algos/AltEdge/data/Soma-Arezzo e TFCO.csv')

        .then(response => response.text())
        .then(csvData => {
            const rows = csvData.split('\n');

            let names = rows[0].split(';')


            let n1 = names[1]
            let n2 = names[2]
            let n3 = names[3]
            let n4 = names[4]
            let n5 = names[5]



            let datas_px = []
            let n1_d2 = []
            let n2_d2 = []
            let n3_d2 = []
            let n4_d2 = []
            let n5_d2 = []



            for (const row of rows) {
                let row2 = row.split(';')

                for (var i = 1; i < row2.length; i++) {

                    row2[i] = row2[i].replace('.', '')
                    row2[i] = parseFloat(row2[i]);
                }

                datas_px.push(row2[0])
                n1_d2.push(row2[1])
                n2_d2.push(row2[2])
                n3_d2.push(row2[3])
                n4_d2.push(row2[4])
                n5_d2.push(row2[5])

            }


            datas_px.shift()
            n1_d2.shift()
            n2_d2.shift()
            n3_d2.shift()
            n4_d2.shift()
            n5_d2.shift()



            Highcharts.chart('gtmoda', {


                title: {
                    text: 'Fashion Retail Interest',
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
                    data: n1_d2,
                }, {
                    name: n2,
                    data: n2_d2,
                }, {
                    name: n3,
                    data: n3_d2,
                }, {
                    name: n4,
                    data: n4_d2,
                }, {
                    name: n5,
                    data: n5_d2,
                },],

                credits: {
                    enabled: false
                },

            });


        });
}

function trendecommerce() {
    fetch('https://kevenwm.github.io/quant_ven/Python Algos/AltEdge/data/Varejistas e-commerce.csv')

        .then(response => response.text())
        .then(csvData => {
            const rows = csvData.split('\n');

            let names = rows[0].split(';')


            let n1 = names[1]
            let n2 = names[2]
            let n3 = names[3]
            let n4 = names[4]
            let n5 = names[5]



            let datas_px = []
            let n1_d2 = []
            let n2_d2 = []
            let n3_d2 = []
            let n4_d2 = []
            let n5_d2 = []



            for (const row of rows) {
                let row2 = row.split(';')

                for (var i = 1; i < row2.length; i++) {

                    row2[i] = row2[i].replace('.', '')
                    row2[i] = parseFloat(row2[i]);
                }

                datas_px.push(row2[0])
                n1_d2.push(row2[1])
                n2_d2.push(row2[2])
                n3_d2.push(row2[3])
                n4_d2.push(row2[4])
                n5_d2.push(row2[5])

            }


            datas_px.shift()
            n1_d2.shift()
            n2_d2.shift()
            n3_d2.shift()
            n4_d2.shift()
            n5_d2.shift()



            Highcharts.chart('gtecommerce', {


                title: {
                    text: 'E-Commerce Brazil Interest',
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
                    data: n1_d2,
                }, {
                    name: n2,
                    data: n2_d2,
                }, {
                    name: n3,
                    data: n3_d2,
                }, {
                    name: n4,
                    data: n4_d2,
                }, {
                    name: n5,
                    data: n5_d2,
                },],

                credits: {
                    enabled: false
                },

            });


        });
}

function trendecommerceworld() {
    fetch('https://kevenwm.github.io/quant_ven/Python Algos/AltEdge/data/Varejistas estrangeiras e-commerce.csv')

        .then(response => response.text())
        .then(csvData => {
            const rows = csvData.split('\n');

            let names = rows[0].split(';')


            let n1 = names[1]
            let n2 = names[2]
            let n3 = names[3]
            let n4 = names[4]
            let n5 = names[5]



            let datas_px = []
            let n1_d2 = []
            let n2_d2 = []
            let n3_d2 = []
            let n4_d2 = []
            let n5_d2 = []



            for (const row of rows) {
                let row2 = row.split(';')

                for (var i = 1; i < row2.length; i++) {

                    row2[i] = row2[i].replace('.', '')
                    row2[i] = parseFloat(row2[i]);
                }

                datas_px.push(row2[0])
                n1_d2.push(row2[1])
                n2_d2.push(row2[2])
                n3_d2.push(row2[3])
                n4_d2.push(row2[4])
                n5_d2.push(row2[5])

            }


            datas_px.shift()
            n1_d2.shift()
            n2_d2.shift()
            n3_d2.shift()
            n4_d2.shift()
            n5_d2.shift()



            Highcharts.chart('gtecommerceworld', {


                title: {
                    text: 'E-Commerce Worldwide Interest in Brazil',
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
                    data: n1_d2,
                }, {
                    name: n2,
                    data: n2_d2,
                }, {
                    name: n3,
                    data: n3_d2,
                }, {
                    name: n4,
                    data: n4_d2,
                },],

                credits: {
                    enabled: false
                },

            });


        });
}

function trendesporte() {
    fetch('https://kevenwm.github.io/quant_ven/Python Algos/AltEdge/data/Varejo esportivo.csv')

        .then(response => response.text())
        .then(csvData => {
            const rows = csvData.split('\n');

            let names = rows[0].split(';')


            let n1 = names[1]
            let n2 = names[2]
            let n3 = names[3]
            let n4 = names[4]
            let n5 = names[5]



            let datas_px = []
            let n1_d2 = []
            let n2_d2 = []
            let n3_d2 = []
            let n4_d2 = []
            let n5_d2 = []



            for (const row of rows) {
                let row2 = row.split(';')

                for (var i = 1; i < row2.length; i++) {

                    row2[i] = row2[i].replace('.', '')
                    row2[i] = parseFloat(row2[i]);
                }

                datas_px.push(row2[0])
                n1_d2.push(row2[1])
                n2_d2.push(row2[2])
                n3_d2.push(row2[3])
                n4_d2.push(row2[4])
                n5_d2.push(row2[5])

            }


            datas_px.shift()
            n1_d2.shift()
            n2_d2.shift()
            n3_d2.shift()
            n4_d2.shift()
            n5_d2.shift()



            Highcharts.chart('gtesporte', {


                title: {
                    text: 'Sports Retail Interest',
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
                    data: n1_d2,
                }, {
                    name: n2,
                    data: n2_d2,
                }, {
                    name: n3,
                    data: n3_d2,
                }, {
                    name: n4,
                    data: n4_d2,
                }, {
                    name: n5,
                    data: n5_d2,
                },],

                credits: {
                    enabled: false
                },

            });


        });
}
function trendlowincome() {
    fetch('https://kevenwm.github.io/quant_ven/Python Algos/AltEdge/data/Vestuário Baixa Renda.csv')

        .then(response => response.text())
        .then(csvData => {
            const rows = csvData.split('\n');

            let names = rows[0].split(';')


            let n1 = names[1]
            let n2 = names[2]
            let n3 = names[3]
            let n4 = names[4]
            let n5 = names[5]



            let datas_px = []
            let n1_d2 = []
            let n2_d2 = []
            let n3_d2 = []
            let n4_d2 = []
            let n5_d2 = []



            for (const row of rows) {
                let row2 = row.split(';')

                for (var i = 1; i < row2.length; i++) {

                    row2[i] = row2[i].replace('.', '')
                    row2[i] = parseFloat(row2[i]);
                }

                datas_px.push(row2[0])
                n1_d2.push(row2[1])
                n2_d2.push(row2[2])
                n3_d2.push(row2[3])
                n4_d2.push(row2[4])
                n5_d2.push(row2[5])

            }


            datas_px.shift()
            n1_d2.shift()
            n2_d2.shift()
            n3_d2.shift()
            n4_d2.shift()
            n5_d2.shift()



            Highcharts.chart('gtlowincome', {


                title: {
                    text: 'Low Income Retail Interest',
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
                    data: n1_d2,
                }, {
                    name: n2,
                    data: n2_d2,
                }, {
                    name: n3,
                    data: n3_d2,
                }, {
                    name: n4,
                    data: n4_d2,
                }, {
                    name: n5,
                    data: n5_d2,
                },],

                credits: {
                    enabled: false
                },

            });


        });
}

$(document).ready(function () {
    trendrent();
    trendjoalherias();
    trendsocial();
    trendmoda();
    trendecommerce();
    trendecommerceworld();
    trendesporte();
    trendlowincome();
});