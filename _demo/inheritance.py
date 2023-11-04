from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('inheritance_index.html')


# http://127.0.0.1:5000
if __name__ == '__main__':
    app.run()