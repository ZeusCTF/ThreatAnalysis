from flask import Flask

app = Flask(__name__)

@app.route("/notmalware")
def hello_world():
    response = 'IyEvYmluL3NoCmhvc3RuYW1lCg=='
    return response, 401

if __name__ == '__main__':
    app.run(debug=True)