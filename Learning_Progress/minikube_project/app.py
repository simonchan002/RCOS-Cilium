# app.py
from flask import Flask
from flask import request
import os
import requests
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Kubernetes!"


@app.route("/greet", methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello, {name}! Welcome to Kubernetes!"
    return '''
        <form method="POST">
            Name: <input type="text" name="name">
            <input type="submit" value="Submit">
        </form>
    '''


@app.route("/info")
def info():
    hostname = os.getenv("HOSTNAME", "Unknown Pod")
    namespace = os.getenv("KUBERNETES_NAMESPACE", "Unknown Namespace")
    return f"""
        <h1>Kubernetes Pod Information</h1>
        <p><b>Pod Name:</b> {hostname}</p>
        <p><b>Namespace:</b> {namespace}</p>
    """


@app.route("/api", methods=["GET"])
def api():
    return {"message": "Hello, Kubernetes!", "status": "success"}



@app.route("/weather/<city>")
def get_weather(city):
    try:
        # Get API key from environment variable
        api_key = os.getenv("a83a56a18dc7dcf62085dab08a06057e")
        if not api_key:
            return jsonify({"error": "API key not configured"}), 500

        # Make the API request
        url = f"http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": api_key,
            "units": "metric"  # Add units for better temperature reading
        }
        
        response = requests.get(url, params=params, timeout=5)  # Add timeout
        
        if response.status_code == 200:
            weather_data = response.json()
            return jsonify({
                "city": weather_data["name"],
                "temperature": weather_data["main"]["temp"],
                "weather": weather_data["weather"][0]["description"],
                "humidity": weather_data["main"]["humidity"]
            })
        elif response.status_code == 404:
            return jsonify({"error": "City not found"}), 404
        else:
            return jsonify({
                "error": f"Weather service error: {response.status_code}"
            }), response.status_code
            
    except requests.exceptions.Timeout:
        return jsonify({"error": "Weather service timeout"}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Weather service error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
