from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("login_get_post.html")


@app.route('/success/<name>')
def success(name):
    code = int(request.args.get('code'))
    return "%d\nwelcome %s" % (code, name)


@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('success', code=1, name=user))
    else:
        user = request.args.get('name')
        return redirect(url_for('success', code=2, name=user))


# http://localhost:5000
# http://localhost:5000/login?name=flask
if __name__ == '__main__':
    app.run()