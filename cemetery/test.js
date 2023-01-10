// Declare the car_name variable
let xcar;

// Get the select element
const select = document.getElementById('result');

// Add an input event listener to the select element
select.addEventListener('input', function () {
    // Get the value of the selected option
    xcar = this.value;
});

var car_name = "Chevrolet S10"


document.getElementById('result2').innerHTML = car_name
