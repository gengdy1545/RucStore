# RucStore 环境配置文档

巧妇难为无米之炊，我们需要先对实验进行一些准备工作，配置好开发环境。
## MySQL
1. 在 [MySQL ZIP Archive](https://dev.mysql.com/downloads/mysql/) 下载压缩包【Windows (x86, 64-bit), ZIP Archive】，并解压到合适的位置。

    ![MySQL 解压目录](../pics/MySQL%20解压目录.png)

2. 将 MySQL 解压目录下的 bin 目录添加到系统环境变量 PATH 中去

3. 在 MySQL 解压目录下创建文件 **`my.ini`**，**basedir** 安装目录调整为自己的安装目录

    ``` shell
    [mysql]
    # 设置mysql客户端默认字符集
    default-character-set=utf8
 
    [mysqld]
    # 设置3306端口
    port = 3306
    # 设置mysql的安装目录
    basedir=C:\\Downloads\\MySQL
    # 设置 mysql数据库的数据的存放目录，MySQL 8+ 不需要以下配置，系统自己生成即可，否则有可能报错
    # datadir=C:\\Downloads\\MySQL\\data
    # 允许最大连接数
    max_connections=20
    # 服务端使用的字符集默认为8比特编码的latin1字符集
    character-set-server=utf8
    # 创建新表时将使用的默认存储引擎
    default-storage-engine=INNODB
    ```

4. 以管理员身份打开命令行，执行如下命令初始化 MySQL

    ```shell
    mysqld  --initialize-insecure （建议使用，不设置root密码）

    mysqld  --initialize --console（不建议使用，在控制台生成一个随机的root密码）
    ```

    如果使用第二条命令进行初始化，则输出的右小角红框内是初始化的密码。

    ![MySQL 初始化](../pics/MySQL%20初始化.png)

5. 安装 mysql 服务

    ``` shell
    //安装 mysql 服务
    mysqld install mysql
 
    //卸载 mysql 服务
    sc delete mysql(需要管理员权限)
 
    //移除 mysql 服务（需要停止 mysql）
    mysqld -remove
    ```

    执行命令成功安装后一般会出现 Service successfully installed

6. 开启 mysql 服务

    ```shell
    // 启动 mysql 服务
    net start mysql

    // 关闭 mysql 服务
    net stop mysql
    ```

    ![MySQL 服务开启](../pics/MySQL%20服务开启.png)

7. 登录 MySQL 并修改密码

    输入如下命令并输入之前红框内密码
    ```shell
    mysql -uroot -p
    ```

    成功登录后修改密码

    ```shell
    //修改root用户的密码
    alter user 'root'@localhost identified by 'newpasswd';
 
    //刷新权限,一般修改密码或授权用户的时候需要使用
    flush privileges;
    ```
    
## Flask

1. 输入如下命令安装 Flask
    ```shell
    pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple
    ```

2. 编写如下代码并运行，可以通过 localhost:5000 访问，页面显示 Hello, World!
    
    ```python
    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    if __name__ == '__main__':
        app.run()
    ```

## Flask 扩展插件
相较于 Djiango，Flask 更加小巧精致，其只保留了核心功能，并通过各种扩展插件来满足我们多种多样的需求。

为了简化数据库操作，推荐使用 **SQLAlchemy**，对数据库的操作都转化成对类属性和方法的操作，在舍弃一些性能开销的同时，换来开发效率的提升。当然也可以使用原汁原味的 **pymysql**，参考 [PyMySQL](_doc/PyMySQL%20简单教程.md)

同时，本次实验的示例还用到了 flask_bcrypt、flask_login、flask_mail、flask_wtf 等 Flask 扩展插件。可以按照如下命令，按照相关 python 包

```shell
pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install flask_sqlalchemy -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install flask_bcrypt -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install flask_login -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install flask_mail -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install flask_wtf -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## Q&A
如果碰到 `ModuleNotFoundError: No module named 'MySQLdb'`，请按照如下命令安装 **mysqlclient**
```shell
pip install mysqlclient -i https://pypi.tuna.tsinghua.edu.cn/simple
```

如果遇到 `Exception: Install 'email_validator' for email validation support`，请按照如下命令安装 **email-validator** 
```shell
pip install email-validator -i https://pypi.tuna.tsinghua.edu.cn/simple
```

如果遇到 `ImportError: cannot import name 'url_decode' from 'werkzeug.urls'`，请安装**特定版本**的 **werkzeug**

```shell
pip install werkzeug==2.3.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## Ubuntu 配置
使用 ubuntu 的同学可以使用如下教程安装 MySQL

1. 更新软件包索引和软件包
    ```shell
    sudo apt update
    sudo apt upgrade
    ```

2. 安装 MySQL

    ```shell
    sudo apt install mysql-server
    ```

3. 检查 MySQL 服务是否正在运行

    ```shell
    sudo systemctl status mysql
    ```

    ![MySQL 配置01](../pics/MySQL%20配置01.png)

4. 配置数据库 root 密码

    默认情况下，MySQL root 用户密码为空。你需要通过运行以下脚本使你的 MySQL 服务器安全：
    ```shell
    sudo mysql_secure_installation
    ```

    系统将询问你是否要安装 “VALIDATE PASSWORD plugin（密码验证插件）”。该插件允许用户为数据库配置强密码凭据。如果启用，它将自动检查密码的强度并强制用户设置足够安全的密码。**禁用此插件是安全的**。但是，必须为数据库使用唯一的强密码凭据。如果不想启用此插件，只需按任意键即可跳过密码验证部分，然后继续其余步骤。

    如果回答是 y，则会要求你选择密码验证级别。可用的密码验证有 “low（低）”、 “medium（中）” 和 “strong（强）”。只需输入适当的数字（0 表示低，1 表示中，2 表示强密码）并按回车键。现在，输入 MySQL root 用户的密码。请注意，必须根据上一步中选择的密码策略，为 MySQL root 用户使用密码。如果你未启用该插件，则只需使用你选择的任意强度且唯一的密码即可。两次输入密码后，你将看到密码强度。如果你确定可以，请按 y 继续提供的密码。如果对密码长度不满意，请按其他任意键并设置一个强密码。

    其余问题，只需要按 y 即可。这将删除匿名用户、禁用 root 远程登录并删除测试数据库。

5. 登录 MySQL

    默认情况下，Ubuntu 系统的 MySQL root 用户为 MySQL 5.7 版本及更新的版本使用插件 auth_socket 设置身份验证。尽管它增强了安全性，但是当你使用任何外部程序（例如 phpMyAdmin）访问数据库服务器时，也会变得更困难。要解决此问题，你需要将身份验证方法从 auth_socket 更改为 mysql_native_password。为此，请使用以下命令登录到你的 MySQL 提示符下：

    ```shell
    sudo mysql
    ```

    要将此身份验证更改为 mysql_native_password 方法，请在 MySQL 提示符下运行以下命令。如果已启用 VALIDATION 插件，请确保已根据当前策略要求使用了强密码。

    ```shell
    ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';

    // 刷新权限
    FLUSH PRIVILEGES;
    ```

    现在我们就可以使用 `mysql -u root -p` 命令登陆 MySQL 了。