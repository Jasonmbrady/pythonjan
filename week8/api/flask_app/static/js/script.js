// var latitude = parseFloat(document.getElementById("lat").innerText)
// var longitude = parseFloat(document.getElementById("lon").innerText)

// fetch(`http://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&units=imperial&appid=1ea00dea84ab8eb870b73d4ae3c33898`)
//     .then(response => response.json())
//     .then(response => {
//         console.log(response);
//         document.getElementById("curr-temp").innerText = response.main.temp;
//         document.getElementById("high-temp").innerText = response.main.temp_max;
//         document.getElementById("low-temp").innerText = response.main.temp_min;
//     })
//     .catch( error => console.log(error))

var myForm = document.getElementById("lat_lon_form");
myForm.onsubmit = function(event){
    event.preventDefault();
    var form = new FormData(myForm);
    fetch("http://localhost:5000/update_user", { method:'POST', body: form })
        .then(res => res.json())
        .then(data => {
            console.log(data);
            document.getElementById("curr-temp").innerText = data.main.temp;
            document.getElementById("high-temp").innerText = data.main.temp_max;
            document.getElementById("low-temp").innerText = data.main.temp_min;
        })
}