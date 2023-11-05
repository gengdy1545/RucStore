# RucStore 项目实现文档
> 尽管项目简单，但涉及的工具使用仍有门槛，教程难免有所疏漏。
> 
> 希望你们可以多多查阅**官方文档**，借助多方工具搜集相关信息，尽其所能理解代码。

- [如何运行和查看本项目的效果](#如何运行和查看本项目的效果)
- [如何学习和理解本项目](#如何学习和理解本项目)
  - [前端框架](#前端框架)
  - [layout 实现](#layout-实现)
    - [\<head\>](#head)
    - [\<body\>](#body)
    - [小结](#小结)
  - [注册和登录](#注册和登录)
    - [table 设计](#table-设计)
    - [注册](#注册)
    - [登录](#登录)
    - [登出](#登出)
- [如何扩展实现本项目](#如何扩展实现本项目)

## 如何运行和查看本项目的效果
* 安装 python3.x 环境
* 按照 [配置文档](RucStore%20配置文档.md) 配置 MySQL 和 Flask

在 mysql 执行 `ruc_store.sql`，可以通过 [source](https://www.runoob.com/mysql/mysql-database-import.html) 命令导入数据。

修改 `src/__init__.py` 文件中 `app.config["SQLALCHEMY_DATABASE_URI"]`，username、password、database 分别对应 MySQL 的用户名、密码和项目所使用的数据库（如果是通过 `ruc_store.sql` 生成的数据库，该项为 **ruc_store**），同时参考 [secret key](https://stackoverflow.com/questions/34902378/where-do-i-get-secret-key-for-flask) 随机生成 `app.config['SECRET_KEY']`

最后在 `src` 目录下执行命令 `python run.py` 运行项目，默认情况下使用 **5000** 端口访问

![ruc_store_1](../pics/ruc_store_1.png)

![ruc_store_3](../pics/ruc_store_3.png)

![ruc_store_4](../pics/ruc_store_4.png)

## 如何学习和理解本项目
* 通过 [Flask 文档](Flask%20简单教程.md) 学习并运行了 _demo
* 必须了解 **flask_login**、**flask_sqlalchemy** 、**flask_wtf** 的使用
  - [flask_login 教程](https://flask-login-cn.readthedocs.io/zh/latest/)
  - [flask_sqlalchemy 教程](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/)
  - [flask_wtf 教程](https://flask-wtf.readthedocs.io/en/1.2.x/quickstart/)
* 通过网上资料加深了对 Python、HTML、CSS、Flask 的理解
  - [Python 教程](https://www.liaoxuefeng.com/wiki/1016959663602400)
  - [HTML 教程](https://www.runoob.com/html/html-tutorial.html)
  - [CSS 教程](https://www.runoob.com/css/css-tutorial.html)
  - [Flask 教程](https://dormousehole.readthedocs.io/en/latest/)

### 前端框架
考虑到同学们的前端知识，本项目实现并不对 HTML 和 CSS 做出过多要求，但是希望大家能借助互联网尝试调整甚至美化界面。

我们使用 Bootstrap 前端框架来大大简化同学们的操作难度。通过 [layout.html](../src/store/templates/layout.html) 文件的第 9 行，我们引入 Bootstrap CSS 文件
```html
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
```

Bootstrap 自带的大部分组件需要原来 JavaScript 才能起作用。具体来说，这些组件依赖 jQuery、Popper 以及他们自己开发的 JavaScript 插件。通过 [layout.html](../src/store/templates/layout.html) 文件的第 80 - 82 行，引入我们需要的 JS 文件

```html
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
```

对于 Bootstrap 的使用，例如 [Alert 组件](https://v4.bootcss.com/docs/components/alerts/)，它能够展示任意长度的文本以及一个可选的关闭按钮。为了展示合适的样式，必须从下列 8 个类（例如 .alert-success）中选择一个合适的并使用。
```html
<div class="alert alert-primary" role="alert">
  A simple primary alert—check it out!
</div>
<div class="alert alert-secondary" role="alert">
  A simple secondary alert—check it out!
</div>
<div class="alert alert-success" role="alert">
  A simple success alert—check it out!
</div>
<div class="alert alert-danger" role="alert">
  A simple danger alert—check it out!
</div>
<div class="alert alert-warning" role="alert">
  A simple warning alert—check it out!
</div>
<div class="alert alert-info" role="alert">
  A simple info alert—check it out!
</div>
<div class="alert alert-light" role="alert">
  A simple light alert—check it out!
</div>
<div class="alert alert-dark" role="alert">
  A simple dark alert—check it out!
</div>
```

![ruc_store_2](../pics/ruc_store_2.png)

可以看到，我们几乎摆脱了繁琐的 CSS 样式调整，只需要简单地引入 `class=alert alert-xxx` 就能够得到美观的页面。对于 Boostrap 的详细使用大家可以参考 [Bootstrap CSS](https://v4.bootcss.com/docs/getting-started/introduction/)。另外，项目中也增加了 [main.css](../src/store/static/main.css) 帮助同学们更好地自定义调成界面。

### layout 实现
正如在 [Flask 文档](Flask%20简单教程.md) 中提到的 Flask 模板继承，我们希望能够尽可能的提高代码复用率，不希望每个页面都重复引入 css 文件和布局代码，所以我们首先实现 [layout.html](../src/store/templates/layout.html) 文件，后面我们实现的所有 HTML 文件都继承或者间接继承自该文件。

#### \<head\>
通过 \<meta\> charset 规定 HTML 文档的字符编码
```html
<meta charset="utf-8">
```

通过 \<meta\> viewport 以便在移动设备上正确显示 (详情可参考 [meta viewport tag](https://stackoverflow.com/questions/51975238/using-html-meta-viewport-tag-with-bootstrap))
```html
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
```

同时我们在 \<head\> 部分引入 [bootstrap css](#前端框架)

#### \<body\>
> 这部分会涉及到后面的一些设计，所以暂时不要求完全搞懂代码，只需要**理解代码逻辑**。
> 等读完后续文档，可以再回头重新理解这部分内容。

在网页设计的时候，我们不妨参考 “**div 梭哈**” 的粗暴方式（注： 这只是盒子布局的例子用法，不能代表盒子布局。而且这种布局已是十年前的用法，现在多采用 HTML5 + CSS3 的方式）

![ruc_store_1](../pics/ruc_store_1.png)

简单举例来说，我们在实现上述页面（最终实现的未登录主页面）的时候，可以将其划分为两部分，分别是**头部 header** 和**主体 main**

在 header 部分 ( [layout.html](../src/store/templates/layout.html)) 的第 18 - 48 行），我们实现简单的 ruc store 标识，Home、Sign in、Register 导航等。如果 Customer 用户登录，需要将 Sign in、Register 导航切换成 Cart、Settings、Logout 导航；如果 Supplier 用户登录，需要将 Sign in、Register 导航切换成 Settings、Logout 导航。

在 main 部分 ( [layout.html](../src/store/templates/layout.html)) 的第 49 - 77 行），我们再次将页面划分为两部分。左边(第 51 - 62 行) 是我们使用的主体，在后续实现中，我们通过模板继承动态实现该部分。右边(第 63 - 75 行) 是用作装饰的侧边栏（**同学可以自己添加功能**）

在 main 部分左边实现中，我们用到了 **Flask 消息闪现**，大家可以通过 [Flask 消息闪现示例](https://dormousehole.readthedocs.io/en/latest/patterns/flashing.html) 来快速理解。

```html
{% with messages = get_flashed_messages(with_categories=true) %}
    {% if messages %}
        {% for category, message in messages %}
            <div class="alert alert-{{ category }}">
                {{ message }}
            </div>
        {% endfor %}
    {% endif %}
{% endwith %}
```

#### 小结
在 layout 实现中，大家重点需要关注的有两点
* 根据登录状态和登录用户来切换 header 内容，请结合后续内容理解
* main 主体部分继承，其实就一句话 `{% block content %}{% endblock %}`

### 注册和登录

* [routes.py](../src/store/routes.py)
* [forms.py](../src/store/forms.py)
* [models.py](../src/store/models.py)
* [layout.html](../src/store/templates/layout.html)
* [login.html](../src/store/templates/login.html)
* [register.html](../src/store/templates/register.html)

#### table 设计
在设计之前，我们首先需要明确自己需要**实现哪些功能**？实现这些功能我们**需要哪些依赖**？针对这个项目的注册登录，我们可能需要实现如下功能：
* Customer 注册登录
* Supplier 注册登录
* **用户 session 的管理**

Customer 和 Supplier 的注册登录可以分别使用 Customer、Supplier 两个 table 来记录他们的 username、password 等信息，而用户 session 的管理，我们需要借助 [Flask_login](https://flask-login-cn.readthedocs.io/zh/latest/) 并定义 User 类来管理

在 [models.py](../src/store/models.py) 文件中我们定义 Customer、Supplier 类。同时我们将 **email 列的 unique 属性设置为 true**，将其作为 Customer(Supplier) 的一个唯一性标识，即不允许 Customer(Supplier) 用户的 email 重复。
```python
class Customer(db.Model,UserMixin):
    __tablename__ = "Customer"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=False,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    password = db.Column(db.String(60),nullable=False)
    consignee = db.Column(db.String(20),nullable=False,default="null")
    address = db.Column(db.String(40),nullable=False,default="null")
    telephone = db.Column(db.String(20),nullable=False,default="null")


class Supplier(db.Model,UserMixin):
    __tablename__ = "Supplier"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20),unique=False,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    password = db.Column(db.String(60),nullable=False)
    shipper = db.Column(db.String(40),nullable=False,default="null")
    address = db.Column(db.String(40),nullable=False,default="null")
    telephone = db.Column(db.String(20),nullable=False,default="null")
```

另外，我们实例化 User 类，主键 id 作为 load_user 函数的返回值。通过 table_name 和 table_id 将其与 Customer、Supplier 表联系在一起，即通过 table_name 得到该条目用户属于 Customer 还是 Supplier，通过 table_id 得到该条目用户在 Customer(Supplier) 的具体条目。
```python
@login_manage.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    __tablename__="User"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=False, nullable=False,default="私密")
    email = db.Column(db.String(120), unique=True, nullable=False)
    table_name = db.Column(db.String(20), unique=False, nullable=False)
    table_id = db.Column(db.Integer,nullable=False)
```

#### 注册
![ruc_store_3](../pics/ruc_store_3.png)

在 [route.py](../src/store/routes.py) 文件中，我们访问 **http://localhost:5000** 或者 **http://localhost:5000/home** 即可访问到网站主页。
```python
@app.route('/')
@app.route("/home")
def home():
    products = Product.query.all()
    return render_template("home.html", products=products)
```

这里我们暂不关注 home.html 文件的实现，而是查看其继承的 [layout.html](../src/store/templates/layout.html) 文件。我们需要设置在未登录界面时**导航栏的 Register 导航跳转**(第 42 行)，这里 url_for('register') 即对应 [route.py](../src/store/routes.py) 中 register 函数的实现
```html
<a class="nav-item nav-link" href="{{ url_for('register') }}">Register</a>
```

在 [forms.py](../src/store/forms.py) 文件中，我们定义注册界面的 form
```python
class RegistrationForm(FlaskForm):
    role=SelectField("Select role", coerce=str, choices=[("1","Customer"), ("2","Supplier")])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
```

由于我们将 email 作为一个唯一性标识，所以在 RegistrationForm 类中增加邮箱验证函数 validate_email，判断他所在用户表内是否已经存在用户使用了该邮箱
```python
    def validate_email(self, email):
        if self.role.data == "1":
            table = Customer
        elif self.role.data == "2":
            table = Supplier
        if table.query.filter_by(email=email.data).first():
            raise ValidationError("Duplicate email")
```

在 [register.html](../src/store/templates/register.html) 文件中我们实现其前端效果，以 RegistrationForm 中的 email 为例(对应 registre.html 第 34 - 46 行)，因为 validators=[DataRequired(), Email()]，所以会判断 email 是否为空且是否符合邮箱格式。同时因为我们定义了 validata_email 函数，所以还会判断该邮箱是否被其他用户使用了。如果不符合要求，form.role.errors 则不为空，我们会将 form.role 增加 [class=is-invalid](https://bootstrapshuffle.com/cn/classes/forms/is-invalid)，同时显示 error 
```html
<div class="form-group">
    {{ form.role.label(class="form-control-label") }}
    {% if form.role.errors %}
        {{ form.role(class="form-control form-control-lg is-invalid") }}
         <div class="invalid-feedback">
            {% for error in form.role.errors %}
                <span>{{ error }}</span>
            {% endfor %}
        </div>
    {% else %}
        {{ form.role(class="form-control form-control-lg") }}
    {% endif %}
</div>
```

最后我们在 [route.py](../src/store/routes.py) 定义视图函数 register。如果我们提交表单的数据满足 validators 且没有抛出异常（例如 validate_email 在邮箱已使用时会抛出异常），则 form.validate_on_submit() == True，然后我们根据表单数据插入 Customer(Supplier) 和 User 表合适的条目。这里，我们用到了 bcrypt 对 password 进行加密。
```python
@app.route("/register",methods=["GET", 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.role.data == "1":
            role = Customer()
            table_name = "Customer"
            table = Customer
        elif form.role.data == "2":
            role = Supplier()
            table_name = "Supplier"
            table = Supplier
        hashed_password = bcrypt.generate_password_hash(password=form.password.data).decode("utf-8")
        role.username = form.username.data
        role.email = form.email.data
        role.password = hashed_password
        db.session.add(role)
        db.session.commit()
        user = User()
        user.table_name = table_name
        user.table_id = table.query.filter_by(email=form.email.data).first().id
        user.username=form.username.data
        user.email=form.email.data
        db.session.add(user)
        db.session.commit()
        flash('Your account was created successfully', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
```

#### 登录
![ruc_store_4](../pics/ruc_store_4.png)

在 [layout.html](../src/store/templates/layout.html) 文件,我们需要设置在未登录界面时**导航栏的 Sign in 导航跳转**(第 41 行)，这里 url_for('login') 即对应 [route.py](../src/store/routes.py) 中 login 函数的实现
```html
<a class="nav-item nav-link" href="{{ url_for("login") }}">Sign in</a>
```

在 [forms.py](../src/store/forms.py) 文件中，我们定义登录界面的 form，在这里我们并不定义相关 validate 函数进行登录验证，而是在表单提交之后交给视图函数 login
```python
class LoginForm(FlaskForm):
    role = SelectField("Select role",coerce=str,choices=[("1","Customer"),("2","Supplier")])
    email = StringField('Mail',validators=[DataRequired(), Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField('Sign in')
```

在 [login.html](../src/store/templates/login.html) 文件中我们实现其前端效果

最后我们在 [route.py](../src/store/routes.py) 定义视图函数 login。如果我们提交表单的数据满足 validators 且没有抛出异常，则 form.validate_on_submit() == True，然后我们根据表单数据选择对应用户的 table 查询用户和密码是否正确。因为我们将 email 作为了一个唯一性标识，所以我们不妨选择 email 来进行查询，即 `table.query.filter_by(email=form.email.data).first()`，非空则说明用户存在。同时，对比用户密码是否正确 `bcrypt.check_password_hash(user.password, form.password.data)`。如果都没问题，我们使用 login_user 函数登录。登录不成功则使用 flash 消息闪现

![ruc_store_5](../pics/ruc_store_5.png)

#### 登出
在用户登录后，可以看到 header 导航栏有 log out 选项

![ruc_store_6](../pics/ruc_store_6.png)

我们在视图函数 logout 中实现，使用 logout_user() 登出即可
```python
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
```

## 如何扩展实现本项目
本项目相比于现在成熟的购物系统，还有很多很多不足，同学们可以结合实际情况丰富功能或者重构项目。这里提供一些思路抛砖引玉
* 顾客多个收货地址管理
* 商家店员雇佣管理
* 存在订单的商品下架（这可以视为本项目的一个 bug）
* 丰富商品信息，增加图片、类别等
* 商品推荐系统
* ……