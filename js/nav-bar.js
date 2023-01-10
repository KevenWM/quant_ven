
function loadnav() {

    let navbar = document.querySelector("#navbarmenu")

    navbar.innerHTML = `<div class="bg-dark">
    <div class="container">
        <nav class="navbar navbar-expand-md navbar-dark bg-dark">
            <div class="container-fluid">
                <a class="navbar-brand text-light" href="index.html">
                    <img class="m" src="img/v-logobranco.png" alt="Icon" width="60" height="60"
                        class="d-inline-block align-text-top">
                    Vêneto Alt
                </a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                    data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false"
                    aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse " id="navbarNav">
                    <ul class="navbar-nav ms-auto ">
                        <li class="nav-item ">
                            <a class="nav-link " aria-current="page" href="index.html">Início</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="graph.html">Gráficos</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="database.html">Databases</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="tools.html">Ferramentas</a>
                        </li>

                    </ul>
                </div>
            </div>
        </nav>
    </div>
</div>`


}