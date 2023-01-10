document.addEventListener('DOMContentLoaded', () => {


    let classe = 'Drogarias'

    function carregar_mapa(classe) {

        if (classe === 'Drogarias') {
            let code_map = '<iframe src="../map.html" frameborder="0" class="map"></iframe>'
            document.getElementById('map-iframe').innerHTML = code_map;
        }
        else {
            let code_map2 = '<iframe src="../map_jewels.html" frameborder="0" class="map"></iframe>'
            document.getElementById('map-iframe').innerHTML = code_map2;
        }


    }

    carregar_mapa(classe)


    const select2 = document.querySelector('#map-select');


    select2.addEventListener('input', function () {
        // Get the value of the selected option

        let xcar = this.value;
        var classe = xcar;

        console.log(classe)

        carregar_mapa(classe)


    });

})

