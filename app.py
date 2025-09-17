import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    message = os.getenv("FLASK_MESSAGE", "Hi, Welcome!")
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
