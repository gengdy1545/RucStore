from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    my_name = 'flask'
    return render_template('hello_template.html', name=my_name)


if __name__ == '__main__':
    app.run()