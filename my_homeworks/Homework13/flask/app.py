# flask_web/app.py
from flask import Flask, render_template, request, jsonify, Response
import requests
from config import Config

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    return render_template("homepage.html")


@app.route('/search', methods=['POST'])
def search_weather():

    cities = request.form.getlist("cities")
    weather_data = []

    for index, city in enumerate(cities):

        querystring = {"q": city, "cnt": "1", "mode": "null", "lon": "0", "type": "link, accurate", "lat": "0",
                       "units": "metric"}

        headers = {
            'x-rapidapi-key': Config.WEATHER_API_KEY,
            'x-rapidapi-host': Config.WEATHER_API_HOST,
        }

        response = requests.request("GET", Config.WEATHER_API_URL, headers=headers, params=querystring)

        if response.status_code == 200:
            data = response.json()
            weather = data['list'][0]
            weather_data.append(weather)

        else:
            return Response(status=response.status_code)

        if index == len(cities) - 1:
            return render_template("weather.html", weather_data=weather_data)

        continue


@app.route('/search_by_location', methods=['POST'])
def search_by_location():

    longitude = request.form.get("lon")
    latitude = request.form.get("lat")

    querystring = {"q": "", "cnt": "1", "mode": "null", "lon": longitude, "type": "link, accurate", "lat": latitude,
                   "units": "metric", 'country': 'UA'}

    headers = {
        'x-rapidapi-key': Config.WEATHER_API_KEY,
        'x-rapidapi-host': Config.WEATHER_API_HOST,
    }

    response = requests.request("GET", Config.WEATHER_API_URL, headers=headers, params=querystring)

    if response.status_code == 200:

        data = response.json()
        weather = data['list']
        return render_template('weather.html', weather_data=weather)

    return Response(status=response.status_code)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
