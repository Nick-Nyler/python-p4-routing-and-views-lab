#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return  "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/hello")
def print_routes():
    print("hello")
    return 'hello'

@app.route('/count/<int:parameter>')
def count(parameter):
    return '\n'.join(str(i) for i in range(parameter)) + '\n'

@app.route('/math/<int:num1>/<operator>/<int:num2>')
def math(num1,operator,num2):
    if operator == '+':
        return str(num1 + num2)
    elif operator == '-':
        return str(num1 - num2)
    elif operator == '*':
        return str(num1 * num2)
    elif operator == 'div':
        return str(num1 / num2)
    elif operator == '%':
        return str(num1 % num2)
    else:
        return 'Invalid operator', 400



if __name__ == '__main__':
    app.run(port=5555, debug=True)