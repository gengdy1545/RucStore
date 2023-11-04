# Flask 简单教程

Flask 是一个用 Python 编写的 Web 应用程序框架，它可以让你高效地编写 Web 程序。Web 程序即“网站”或“网页程序”，是指可以通过浏览器进行交互的程序。我们日常使用浏览器访问的B站、知乎、必应等网站都是 Web 程序。

Flask 是典型的微框架，作为 Web 框架来说，它仅保留了核心功能：请求响应处理
和模板渲染。这两类功能分别由 Werkzeug（WSGI 工具库）完成和 Jinja（模板渲
染库）完成。

因为Flask自带了一个Web服务器，是在其必备依赖 Werkzeug 中实现的。所以在开发时，可以直接启动服务，而不需要通过 Tomcat 或 Apache。不过由于内置服务器自身处理能力有限，在生产环境中还是需要使用其他的Web服务器，这也是Flask官方建议的。

## Flask 路由

Flask 中的 **route()** 用于将 URL 绑定到函数。如下所示，URL '/hello' 绑定到 hello_world() 函数。如果浏览器访问 http://localhost:5000/hello ，将显示 Hello, World!。

```python
# 具体可参考 _demo/hello.py
@app.route('/hello')
def hello_world():
    return 'Hello, World!'
```

通过向规则参数添加变量部分，可以构建动态 URL。此变量部分标记为 <variable_name>。如下所示，如果在浏览器中访问 http://localhost:5000/hello/Flask ，将显示 Hello, Flask!。

```python
# 具体可参考 _demo/hello_name.py
@app.route('/hello/<name>')
def hello_name(name):
    return 'hello %s!' % name
```

## Flask URL 构建
**url_for()** 函数接受函数的名称作为第一个参数，以及若干个关键字参数作为函数的参数。如下所示，hello_user 函数检查接受的参数是否与 admin 匹配。如果匹配则使用 url_for 重定向到 hello_admin 函数，否则重定向到将接受的 name 参数作为 guest 参数的 hello_guest 函数。如果在浏览器中访问 http://localhost:5000/user/admin ，将显示 Hello Admin，如果访问 http://localhost:5000/user/flask ，将显示 Hello flask as Guest。

```python
# 具体可参考 _demo/hello_url_for.py
@app.route('/admin')
def hello_admin():
    return 'Hello Admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest


@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest = name))
```

## Flask 模板
模板其实是一个包含相应文本的文件，其中用占位符（变量）表示动态部分，告诉模板引擎其具体的值需要从使用的数据中获取。使用真实值替换变量，再返回最终得到的字符串，这个过程称为渲染。

在项目下创建 temlates 文件夹，用于存放所有模板文件。在 template 目录下创建一个模板文件 hello_template.html, 内容如下：

```html
<!-- 具体可参考 _demo/templates/hello_template.html -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body>
    <p>welcome {{ name }}</p>
</body>
</html>
```

代码中传入字符串给模板（当然也可以传列表，字典等）

```python
# 具体可参考 _demo/hello_template.py
@app.route('/')
def index():
    my_name = 'flask'
    return render_template('hello_template.html', name=my_name)
```

> **<big>Tips</big>**
> 
> 乍一看，render_template 似乎就是之前使用的重定向函数 redirect，redirect 将 URL 变成重定向的 URL，但是 render_template 则不会改变 URL，而是将动态数据和静态 HTML 模板结合实现页面的动态展示。

## Flask 模板继承
Jinja(Flaks 模板渲染库)最有力的部分就是模板继承。模板继承允许你创建一个基础“骨架模板”，这个模板中包含站点的常用元素，定义可以被子模块继承的 block

在下面的 html 文件中，`{% block %}` 标记定义了两个可以被子模板填充的块。block 标记告诉模板渲染引擎这是一个可以被子模板重载的部分。

```html
<!-- 具体可参考 _demo/templates/inheritance_layout.html -->
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}{% endblock %} - My Webpage</title>
</head>
<body>
    <div id="content">{% block content %}{% endblock %}</div>
</body>
</html>
```

子模板如下所示，这里的 `{% extends %}` 标记是关键，它告诉模板渲染引擎这个模板“扩展”了另一个模板。
```html
<!-- 具体可参考 _demo/templates/inheritance_index.html -->
{% extends "layout.html" %}
{% block title %}Index{% endblock %}
{% block content %}
    <h1>Index</h1>
    <p>Welcome on my awesome homepage.</p>
{% endblock %}
```

运行如下的 python 文件，访问 http://127.0.0.1:5000 我们可以看到继承了 layout 页面的 index 页面

```python
具体可参考 _demo/inheritance.py
@app.route('/')
def index():
    return render_template('inheritance_index.html')
```

## Flask 静态文件

Web 应用程序通常需要静态文件，例如 JS 文件或支持网页显示的 CSS 文件，这些文件是从包或者 static 文件夹中提供。

在下面示例中，在 hello_static.html 中的 HTML 按钮的 OnClick 事件上调用 hello_static.js 中定义的 sayHello 函数。

```html
<!-- 具体可参考 _demo/templates/hello_static.html -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <script type = "text/javascript" src = "{{ url_for('static', filename = 'js/hello_static.js') }}">
    </script>
</head>
<body>
    <input type = 'button' onclick = "sayHello()" value = "Say Hello" />
</body>
</html>
```

```javascript
// 具体可参考 _demo/static/js/hello_static.js
function sayHello() {
    alert("Hello world")
}
```

```python
# 具体可参考 _demo/hello_static.py
@app.route('/')
def index():
    my_name = 'flask'
    return render_template('hello_template.html', name=my_name)
```

## Flask HTTP 方法

**GET** 和 **POST** 是常见的 http 方法。GET 方法主要用于请求数据，而 POST 方法主要用于提交数据。当需要传递数据时，尽可能使用 POST 方法，避免使用 GET 方法传递敏感数据。

默认情况下，Flask 路由响应 GET 请求。如下例子演示两种访问方式：

当我们访问 http://localhost:5000 正常提交表单时，由于 html 中指定了 method 为 post，所以会调用 login() 函数中的 if 语句，执行 POST 方法的代码，返回 code 为 1 的 success 页面。而如果我们直接访问 http://localhost:5000/login?name=flask ，则会调用 else 语句，执行 GET 方法的代码，返回 code 为 2 的 success 页面。

```html
<!-- 具体可参考 _demo/templates/login_get_post.html -->
<form action = "http://localhost:5000/login" method = 'post'>
    <p>Enter Name:</p>
    <p><input type='text' name='name'/></p>
    <p><input type='submit' value='submit'/></p>
</form>
```

```python
# 具体可参考 _demo/login_get_post.py
@app.route('/')
def index():
    return render_template("login.html")


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
```

## Flask 发送表单数据

在下列示例中，‘/’ URL 呈现具有表单的网页 student.html。填入的数据发布到 '/result' URL，其触发 result() 函数，result() 函数收集字典对象中的 request.from 中存在的表单数据，并将其发送给 result.html

```html
<!-- 具体可参考 _demo/templates/student.html -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body>
<form action="http://localhost:5000/result" method="POST">
    <p>Name <input type="text" name="Name"/></p>
    <p>Physics <input type="text" name="Physics"/></p>
    <p>Chemistry <input type="text" name="Chemistry"/></p>
    <p>Maths <input type="text" name="Mathematics"/></p>
    <p><input type="submit" value="submit"/></p>
</form>
</body>
</html>
```

```python
# 具体可参考 _demo/student.py
@app.route('/')
def student():
    return render_template('student.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result=result)
```

```html
<!-- 具体可参考 _demo/templates/result.html -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
</head>
<body>
<table>
    {% for key, value in result.items() %}
    <tr>
        <th>{{ key }}</th>
        <th>{{ value }}</th>
    </tr>
    {% endfor %}
</table>
</body>
</html>
```

## Flask Cookies
设置 cookies，默认有效期是临时 cookie，浏览器关闭就失效。可以通过 max_age 设置有效期
```python
resp = make_response("success") 
resp.set_cookie("key", "value", max_age=3600)
```

获取 cookie，通过 request.cookies 的方式，返回的是一个字典，可以获取字典里的相应值
```python
cookie_1 = request.cookies.get("key")
```

删除 cookie，这里说的删除只是让 cookie 过期，通过 delete_cookie 的方式，里面是 cookie 的名字
```python
resp = make_response("del success")
resp.delete_cookie("key")
```

## Flask Session
由于 HTTP 协议是无状态的协议，所以服务端需要记录用户的状态时，就需要用某种机制来识别具体的用户，这个机制就是 Session。典型的场景比如购物车，当你点击下单按钮时，由于 HTTP 协议无状态，所以并不知道是哪个用户操作的，所以服务端要为特定的用户创建特定的 Session 用于标识这个用户，并跟踪这个用户，这样才知道购物车里有什么东西。

Session 对象是一个字典对象，设置和释放一个变量如下：
```python
# 设置一个 username 变量
session['username'] = 'admin'

# 释放该变量
seesion.pop('username', None)
```

下面这个例子是 Flask Session 的简单演示。Flask 应用程序需要一个定义的 SECRET_KEY，'/' URL 在未登陆时提示用户登陆，通过点击超链接跳转到 '/login' 界面，注意 href 跳转按照 GET 方式，所以将打开一个登陆表单。form 的 action 为空，提交后仍由当前页处理，所以再次回到 '/login'，但此时是 POST 方式，所以重定向到 '/' 页面。此时 session['username'] 已经设置，所以将呈现用户名。点击注销按钮，跳转到 '/logout' 注销该变量并再次回到 '/'

```python
# 具体可参考 _demo/session.py
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
```

## Flask 文件上传
可以在 Flask 对象的配置设置中定义默认上传文件夹的路径和上传文件的最大大小，例如上传到 upload 文件夹，则定义 app.config['UPLOAD_FOLDER'] = 'upload/'，upload 前面没有 '/'

```python
app.config['UPLOAD_FOLDER'] # 定义上传文件夹的路径
app.config['MAX_CONTENT_LENGTH'] # 定义上传文件的最大大小
```

使用 Flask 上传文件时，HTML 表单的 enctype 属性需要设置为 'multipart/form-data', URL 处理程序从 request.files[] 对象中提取文件并将其保存到所需的位置。每个上传的文件首先会保存在服务器上的临时位置，然后将其实际保存到它的最终位置。目标文件的名称可以从 request.files[file] 对象的 filename 属性中获取，但是建议使用 secure_filename() 函数获取它的安全版本
