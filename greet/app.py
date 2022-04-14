from flask import Flask

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
            <a href="/welcome">suprise page</a>
            <a href="/welcome/home">another suprise</a>
            <a href="/welcome/back">third suprise</a>
        </body>
        </html>
    """
    return html

@app.route('/welcome')
def welcome():
    return f"""
    <h2>you reached the welcome page</h2>
    <a href="/"><button>Home</button></a>
    """

@app.route('/welcome/home')
def welcome_home():
    return f"""
    <h2>welcome home you filthy animal</h2>
    <a href="/"><button>Home</button></a>
    """

@app.route('/welcome/back')
def welcome_back():
    return f"""
    <h2>welcome back, you sly dog</h2>
    <a href="/"><button>Home</button></a>
    """