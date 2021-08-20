from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('hello.html')


@app.route('/calc')
def calculator():
    return render_template('calculator.html')


@app.route('/calc/<int:x>/<int:y>/<string:operation>')
def calculation(x, y, operation):

    if operation.lower() in ['sum', 'add',  '+']:
        return render_template('calculation.html', x=x, y=y, operation=x + y, sign='+')

    elif operation.lower() in ['difference', 'dif', '-']:
        return render_template('calculation.html', x=x, y=y, operation=x - y, sign='-')

    elif operation.lower() in ['multiply', 'mult', '*']:
        return render_template('calculation.html', x=x, y=y, operation=x * y, sign='*')

    elif operation.lower() in ['divide', 'div', '/']:
        if y == 0:
            return render_template('ZeroDivisionError.html')
        return render_template('calculation.html', x=x, y=y, operation=x / y, sign='/')

    else:
        return render_template('ValueError.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
