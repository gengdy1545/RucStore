# RucStore
```
  ____  _   _  ____ ____ _____ ___  ____  _____ 
 |  _ \| | | |/ ___/ ___|_   _/ _ \|  _ \| ____|
 | |_) | | | | |   \___ \ | || | | | |_) |  _|  
 |  _ <| |_| | |___ ___) || || |_| |  _ <| |___ 
 |_| \_\\___/ \____|____/ |_| \___/|_| \_\_____|
```
**RucStore** 是一个极其简化的购物系统，用于《数据库系统概论》实验教学。

## 实验环境：
- 数据库：MySQL
- 编程语言：Python
- Web 框架：Flask
- 前端框架: Bootstrap
- 推荐编辑器：VSCode

## 项目说明
RucStore 实现了注册登录、商品交易等功能，按照 [配置文档](_doc/RucStore%20配置文档.md) 配置环境

进入到 `src` 文件夹下，修改 `__init__.py` 文件中 `app.config["SQLALCHEMY_DATABASE_URI"]`，同时参考 [secret key](https://stackoverflow.com/questions/34902378/where-do-i-get-secret-key-for-flask) 随机生成 `app.config['SECRET_KEY']`


在运行之前请在 mysql 执行 `ruc_store.sql`，执行命令 `python run.py` 运行项目，默认情况下使用 **5000** 端口访问