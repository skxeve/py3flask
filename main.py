from flask import Flask

app = Flask(__name__)
mode_debug = True


@app.route('/')
def index():
    return 'Hello Flask!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=mode_debug)
