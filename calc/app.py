from flask import Flask, request
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
            <a href="/add"><button>Add</button></a>
            <a href="/sub"><button>Subtract</button></a>
            <a href="/mult"><button>Multiply</button></a>
            <a href="/div"><button>Divide</button></a>            
        </body>
        </html>
    """
    return html

@app.route('/add')
def add_inputs():
    return """
    <form method="POST">
        <input type="number" placeholder="a" name="a" />
        <input type="number" placeholder="b" name="b" />
        <button>Add</button>
    </form>
    """

@app.route('/add', methods=['POST'])
def add():
    first = request.form['a']
    second = request.form['b']
    answer = operations.add(first, second)
    return f"""
    <h1>{answer}</h1>
    <a href="/"><button>Home</button></a>
    """

@app.route('/sub')
def sub_inputs():
    return """
    <form method="POST">
        <input type="number" placeholder="a" name="a" />
        <input type="number" placeholder="b" name="b" />
        <button>Subtract</button>
    </form>
    """

@app.route('/sub', methods=['POST'])
def sub():
    first = request.form['a']
    second = request.form['b']
    answer = operations.sub(first, second)
    return f"""
    <h1>{answer}</h1>
    <a href="/"><button>Home</button></a>
    """

@app.route('/mult')
def mult_inputs():
    return """
    <form method="POST">
        <input type="number" placeholder="a" name="a" />
        <input type="number" placeholder="b" name="b" />
        <button>Multiply</button>
    </form>
    """

@app.route('/mult', methods=['POST'])
def mult():
    first = request.form['a']
    second = request.form['b']
    answer = operations.mult(first, second)
    return f"""
    <h1>{answer}</h1>
    <a href="/"><button>Home</button></a>
    """

@app.route('/div')
def div_inputs():
    return """
    <form method="POST">
        <input type="number" placeholder="a" name="a" />
        <input type="number" placeholder="b" name="b" />
        <button>Divide</button>
    </form>
    """

@app.route('/div', methods=['POST'])
def div():
    first = request.form['a']
    second = request.form['b']
    answer = operations.div(first, second)
    return f"""
    <h1>{answer}</h1>
    <a href="/"><button>Home</button></a>
    """