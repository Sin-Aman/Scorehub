from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == "__flasktest__":
    app.run(host="127.0.0.1", port=8080, debug=True)