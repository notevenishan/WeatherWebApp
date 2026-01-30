from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "7278a08a4648f4ee1e2441acf90e991b"  # Replace with your OpenWeatherMap key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            data = response.json()
            if data.get("cod") == 200:
                weather_data = {
                    "city": city,
                    "temp": data["main"]["temp"],
                    "desc": data["weather"][0]["description"].title(),
                    "humidity": data["main"]["humidity"],
                    "wind": data["wind"]["speed"]
                }
            else:
                weather_data = {"error": data.get("message", "City not found")}
    return render_template("index.html", weather=weather_data)

if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000)
