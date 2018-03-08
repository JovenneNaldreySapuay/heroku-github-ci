from flask import Flask
app = Flask(__new__)

@app.route('/')
def index():
    return 'hello, world'
