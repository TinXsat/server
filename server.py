"""
I guess that's the only file that will ever be here haha
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_there():
    return 'Hello from TinX server!'


if __name__ == '__main__':
    app.run()
