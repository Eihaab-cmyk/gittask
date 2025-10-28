const API_KEY = "9a23c391f3ae482a822102229252810";
let city = "";
var recentSearches = [];

// ---------- Closure for search history ----------
function createSearchHistory() {
    let history = [];

    function updateUI() {
        const container = document.getElementById("recentSearches");
        container.innerHTML = "";

        history.slice(-5).reverse().forEach(cityName => {
            const btn = document.createElement("button");
            btn.textContent = cityName;
            btn.classList.add("recent-btn");
            btn.addEventListener("click", () => {
                document.getElementById("cityInput").value = cityName;
                getWeather(cityName);
            });
            container.appendChild(btn);
        });
    }

    return function addSearch(cityName) {
        if (!history.includes(cityName)) {
            history.push(cityName);
        }
        console.log("Recent Searches:", history);
        updateUI();
    };
}
const addToHistory = createSearchHistory();

// ---------- Fetch Weather Data (Async/Await + Promises) ----------
async function getWeather(cityName) {
    const loader = document.getElementById("loader");
    const output = document.getElementById("output");

    try {
        // show loading spinner
        loader.style.display = "block";
        output.innerHTML = "";

        const response = await fetch(
            `https://api.weatherapi.com/v1/current.json?key=${API_KEY}&q=${encodeURIComponent(cityName)}&aqi=no`
        );

        if (!response.ok) throw new Error("Failed to fetch weather data");

        const data = await response.json();
        displayWeather(data);
        addToHistory(cityName);

    } catch (error) {
        output.innerHTML = `<p style="color:red;">${error.message}</p>`;
    } finally {
        // hide loader after fetching completes (success or error)
        loader.style.display = "none";
    }
}

// ---------- Display Weather ----------
function displayWeather(data) {
    const output = document.getElementById("output");

    const temp = data?.current?.temp_c ?? "N/A";
    const desc = data?.current?.condition?.text ?? "unknown";
    const location = data?.location?.name ?? "Unknown";

    const displayData = { ...data, temperature: temp, condition: desc, location: location };

    output.innerHTML = `
        <h3>${displayData.location}</h3>
        <p>Temperature: ${displayData.temperature}°C</p>
        <p>Condition: ${displayData.condition}</p>
    `;
}

// ---------- Event Listener ----------
document.getElementById("getWeather").addEventListener("click", () => {
    const input = document.getElementById("cityInput");
    city = input.value.trim();

    if (!city) {
        alert("Please enter a city name!");
        return;
    }

    getWeather(city);
});
