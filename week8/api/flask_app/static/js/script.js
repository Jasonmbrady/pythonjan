var latitude = parseFloat(document.getElementById("lat").innerText)
var longitude = parseFloat(document.getElementById("lon").innerText)

// fetch(`http://api.openweathermap.org/data/2.5/weather?lat=${latitude}&lon=${longitude}&units=imperial&appid=1ea00dea84ab8eb870b73d4ae3c33898`)
//     .then(response => response.json())
//     .then(response => {
//         console.log(response);
//         document.getElementById("curr-temp").innerText = response.main.temp;
//         document.getElementById("high-temp").innerText = response.main.temp_max;
//         document.getElementById("low-temp").innerText = response.main.temp_min;
//     })
//     .catch( error => console.log(error))