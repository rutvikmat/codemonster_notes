let chart;

document.addEventListener("DOMContentLoaded", () => {
  if (localStorage.getItem("dark") === "true") {
    document.body.classList.add("dark");
  }
  loadWeather();
});

function toggleDarkMode() {
  document.body.classList.toggle("dark");
  localStorage.setItem("dark", document.body.classList.contains("dark"));
}

function loadWeather() {
  navigator.geolocation.getCurrentPosition(async pos => {
    const lat = pos.coords.latitude;
    const lon = pos.coords.longitude;

    // Reverse Geocoding
    const geo = await fetch(
      `https://geocoding-api.open-meteo.com/v1/reverse?latitude=${lat}&longitude=${lon}`
    );
    const geoData = await geo.json();
    document.getElementById("city").innerText =
      geoData.results[0].name + ", " + geoData.results[0].country;

    // Weather + Forecast
    const weather = await fetch(
      `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true&daily=temperature_2m_max,weathercode&timezone=auto`
    );
    const data = await weather.json();

    document.getElementById("current").innerHTML = `
      <h3>${data.current_weather.temperature}°C</h3>
      <p>Wind: ${data.current_weather.windspeed} km/h</p>
    `;

    renderForecast(data.daily);
    renderChart(data.daily.temperature_2m_max);
  });
}

function renderForecast(daily) {
  const forecast = document.getElementById("forecast");
  forecast.innerHTML = "";

  daily.time.slice(0, 7).forEach((day, i) => {
    forecast.innerHTML += `
      <div class="card">
        <p>${day}</p>
        <img src="https://openweathermap.org/img/wn/10d.png" width="40">
        <p>${daily.temperature_2m_max[i]}°C</p>
      </div>
    `;
  });
}

function renderChart(temps) {
  const ctx = document.getElementById("tempChart");
  if (chart) chart.destroy();

  chart = new Chart(ctx, {
    type: "line",
    data: {
      labels: ["D1","D2","D3","D4","D5","D6","D7"],
      datasets: [{
        data: temps,
        borderWidth: 2
      }]
    }
  });
}
