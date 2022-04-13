from crypt import methods

from requests import request
from flask import Flask
import operations

app = Flask(__name__)

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <h1>Flask Practice!</h1>

            <form method="POST">
                <input type="text" placeholder="a" name="a" />
                <input type="text" placeholder="b" name="b" />
                <a href="/add"><button>Add</button></a>
                <a href="/sub"><button>Subtract</button></a>
                <a href="/mult"><button>Multiply</button></a>
                <a href="/div"><button>Divide</button></a>
            </form>
            
        </body>
        </html>
    """
    return html

@app.route('/add', methods=['POST'])
def add():
    first = request.form['a']
    second = request.form['b']
    answer = operations.add(first, second)
    return f"<h1>{answer}</h1>"

@app.route('/sub', methods=['POST'])
def add():
    first = request.form['a']
    second = request.form['b']
    answer = operations.sub(first, second)
    return f"<h1>{answer}</h1>"

@app.route('/mult', methods=['POST'])
def add():
    first = request.form['a']
    second = request.form['b']
    answer = operations.mult(first, second)
    return f"<h1>{answer}</h1>"

@app.route('/div', methods=['POST'])
def add():
    first = request.form['a']
    second = request.form['b']
    answer = operations.div(first, second)
    return f"<h1>{answer}</h1>"