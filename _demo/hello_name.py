from flask import Flask
app = Flask(__name__)


@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' %name


# http://127.0.0.1:5000/hello/flask
if __name__ == '__main__':
    app.run()