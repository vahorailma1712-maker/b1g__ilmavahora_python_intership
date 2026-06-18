const inputbox = document.querySelector('.input-box');
const searchBtn = document.getElementById('searchBtn');
const Weather_img = document. querySelector('.weather.img');
const temperature = document.querySelector('.temperature');
const description= document.querySelector('.description');
const humidity = document.getElementById('.humidity');
const wind_speed = document.getElementById('wind-speed');

const weather_body = document.querySelector('weather-body');




async function checkweather(city){
    const api_key = "d78485184cfd300422bce37e7ff44dca"
    const url = 'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric';
    const weather_data= await factch('${url}').then(response => response.json());
    
    temperature.innerHTML = '${math.round(weather_data.main.temp-273.15)}°C';
    description.innerHTML ='${weather_data.wea[0].description}';


    humidity.innerHTML='${weather_data.main humidity}%';
    wind_speed.innerHTML ='${weather_data.wind.speed}Km/H';
    sweech(weather_data.weather[0].main)
          
    console.log(weather_data);

}

   searchBtn.addEventListener('click',(value)=>{
   checkweather(inputbox.value)
});