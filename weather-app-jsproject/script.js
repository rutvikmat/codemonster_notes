const apiKey = "b4cd0a4a639ada6d372f1e019363a162";

async function getWeather() {
  const city = document.getElementById("city").value;
  const result = document.getElementById("result");

  if (city === "") {
    result.innerHTML = "Please enter a city name";
    return;
  }

  try {
    const response = await fetch(
      `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`
    );

    if (!response.ok) {
      throw new Error("City not found");
    }

    const data = await response.json();

    result.innerHTML = `
      <h3>${data.name}</h3>
      <p>🌡️ Temperature: ${data.main.temp} °C</p>
      <p>🌥️ Weather: ${data.weather[0].description}</p>
      <p>💨 Wind Speed: ${data.wind.speed} m/s</p>
    `;
  } catch (error) {
    result.innerHTML = error.message;
  }
}
