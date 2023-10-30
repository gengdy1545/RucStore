from flask import Flask, session, redirect, url_for, request
app = Flask(__name__)
app.secret_key = 'any random string'


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return '登陆用户名是:' + username + '</br>' + \
            "<b><a href = '/logout'>点击这里注销</a></b>"
    return "您暂未登陆，<br><a href = '/login'></b>点击这里登陆</b></a>"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
    <form action = "" method = "post">
        <p><input type="text" name="username"/></>
        <p><input type="submit" value="login"/></>
    </form>
    '''


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()