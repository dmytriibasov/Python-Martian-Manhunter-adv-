# flask_web/app.py
import requests
from flask import Flask, render_template, request, Response
from flask_restful import Resource, Api
from filehandler import FileHandler
from config import Config

app = Flask(__name__)


@app.route('/', methods=['GET'])
def homepage():
    return render_template("homepage.html")


@app.route('/search', methods=['POST'])
def search_weather():
    city = request.form.get("city")
    querystring = {"q": city, "cnt": "1", "mode": "null", "lon": "0", "type": "link, accurate", "lat": "0",
                   "units": "metric"}

    headers = {
        'x-rapidapi-key': Config.WEATHER_API_KEY,
        'x-rapidapi-host': Config.WEATHER_API_HOST
    }

    response = requests.request("GET", Config.WEATHER_API_URL, headers=headers, params=querystring)
    if response.status_code == 200:
        data = response.json()
        weather = data['list'][0]
        return render_template("weather.html", weather=weather)

    return Response(status=404)


api = Api(app)

todos_file = FileHandler('my_todos.json')
todos = {}


class Todo(Resource):

    def get(self, todo_id):
        try:
            file_data = todos_file.data
            data = {todo_id: file_data[str(todo_id)]}
        except KeyError:
            return Response("Not found", status=404)
        return data

    def put(self, todo_id):
        todos[todo_id] = request.json.get('text')
        todos_file.update(data=todos)
        file_data = todos_file.data
        return {todo_id: file_data[str(todo_id)]}

    def delete(self, todo_id):
        del todos[todo_id]
        todos_file.update(data=todos)
        file_data = todos_file.data
        return Response(file_data, status=204)


class TodoList(Resource):

    def get(self):
        data = todos_file.data
        return data

    def post(self):
        todos[request.json.get('todo_id', None)] = request.json.get('text', "")
        todos_file.update(data=todos)
        file_data = todos_file.data
        return file_data


class WeatherAPI(Resource):

    def get(self):
        weather = []
        cities = request.args.get("city")
        cities = cities.split(',')
        for city in cities:
            querystring = {"q": city, "cnt": "1", "mode": "null", "lon": "0", "type": "link, accurate", "lat": "0",
                           "units": "metric"}

            headers = {
                'x-rapidapi-key': Config.WEATHER_API_KEY,
                'x-rapidapi-host': Config.WEATHER_API_HOST
            }

            response = requests.request("GET", Config.WEATHER_API_URL, headers=headers, params=querystring)
            if response.status_code == 200:
                data = response.json()
                weather.append(data['list'])
            else:
                return Response(status=response.status_code)

        return weather


api.add_resource(WeatherAPI, '/weather')
api.add_resource(Todo, '/todos/<int:todo_id>')
api.add_resource(TodoList, '/todos')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
