async function getLocationWeather() {
  const result = document.getElementById("result");

  if (!navigator.geolocation) {
    result.innerHTML = "Geolocation is not supported by your browser.";
    return;
  }

  result.innerHTML = "📡 Fetching location...";

  navigator.geolocation.getCurrentPosition(
    async (position) => {
      const lat = position.coords.latitude;
      const lon = position.coords.longitude;

      try {
        const response = await fetch(
          `https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current_weather=true`
        );

        const data = await response.json();
        const weather = data.current_weather;

        result.innerHTML = `
          <h3>🌍 Your Location</h3>
          <p>🌡️ Temperature: ${weather.temperature} °C</p>
          <p>💨 Wind Speed: ${weather.windspeed} km/h</p>
        `;
      } catch (error) {
        result.innerHTML = "Failed to fetch weather data.";
      }
    },
    () => {
      result.innerHTML = "❌ Location access denied.";
    }
  );
}
