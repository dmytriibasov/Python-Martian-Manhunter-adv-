from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    return "Welcome!"


@app.route('/hello')
def hello():
    return 'Hi there!'


@app.route('/name')
def name():
    return 'My name is Dmytrii Basov'
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
