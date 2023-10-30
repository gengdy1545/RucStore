# Apache 配置文档
1. 在 [Apache lounge](https://www.apachelounge.com/download/) 下载 Apache xxxx Win64下的 【httpd-xxxx-win64-VSxx.zip】 压缩包，并解压到合适的位置。

2. Apache 解压后的文件目录如下所示
![Apache 文件目录](../pics/Apache%20文件目录.png)

3. 打开 `安装目录\conf\httpd.conf`，修改信息 

`SRVROOT` 修改为 Apache 的安装目录，注意使用的是左斜杠而不是右斜杠
![Apache 配置01](../pics/Apache%20配置01.png)

`ServerName` 修改为 localhost:80

![Apache 配置03](../pics/Apache%20配置03.png)

`DocumentRoot` 修改为自定义的网站根目录，`<Directory ....>` 修改为相同内容

![Apache 配置04](../pics/Apache%20配置04.png)

4. 以管理员身份打开命令行，并进入 bin 路径下，执行如下命令

```shell
\\ Apache24 为我们自定义的服务名
httpd.exe -k install -n "Apache24"
```
![Apache 配置02](../pics/Apache%20配置02.png)

5. 启动 apache 服务

```shell
net start Apache24

// 测试
httpd -n "Apache24" -t
```

6. 在我们自定义的网站根目录下创建文件 index.html

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>hello, world</title>
</head>
<body>
    <h1>我的第一个标题</h1>
    <p>我的第一个段落。</p>
</body>
</html>
```
在浏览器输入 localhost 或者 127.0.0.1，可以看到如下内容
![Apache 测试](../pics/Apache%20测试.png)


## Ubuntu 配置
使用 ubuntu 的同学可以使用如下教程安装 Apache

1. 更新软件包索引和软件包
```shell
sudo apt update
sudo apt upgrade
```

2. 安装 apache
```shell
sudo apt install apache2
```

3. 检查 Apache Web 服务器是否已经运行
```shell
sudo systemctl status apache2
```

![Apache 配置05](../pics/Apache%20配置05.png)

4. Ubuntu 默认使用 ufw 防火墙配置工具，需要调整防火墙允许 Apache Web 服务器

首先，使用如下命令列出 Ubuntu 上可用的应用程序配置文件
 ```shell
sudo ufw app list
 ```

![Apache 配置06](../pics/Apache%20配置06.png)

如上所示，Apache 已安装 ufw 配置文件，我们可以使用 `ufw app info "Profile Name"` 命令列出有关每个配置文件及其包含的规则的信息。

```shell
ufw app info "Apache Full"
```

![Apache 配置07](../pics/Apache%20配置07.png)

如上所示，Apache Full 配置文件指定了应该允许的端口和协议。它还引用了 Apache 的其他应用程序配置文件，其中包含允许的端口和协议。我们可以使用 `ufw allow` 命令允许我们列出的端口和协议。

```shell
// 允许 HTTP 和 HTTPS 通信
sudo ufw allow in "Apache Full"

// 只允许 HTTP 通信
sudo ufw allow in "Apache"
```

现在，打开浏览器并输入 https://localhost，你将看到 Apache2 默认欢迎页面。

![Apache 测试界面](../pics/Apache%20测试界面.png)

5. 修改 Apache 默认网站根目录
Apache 默认网站根目录为 `/var/www/html`，我们可以通过修改 `/etc/apache2/sites-available/000-default.conf` 文件来修改网站根目录。

```shell
sudo vim /etc/apache2/sites-available/000-default.conf
```

同时将 `/etc/apache2/apache2.conf` 文件中的 `Directory` 修改为对应的网站根目录

最后重启 Apache 服务

```shell
sudo systemctl restart apache2
```
