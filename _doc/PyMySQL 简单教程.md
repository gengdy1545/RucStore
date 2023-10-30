# PyMySQL 简单教程

## 安装
```shell
pip3 install PyMySQL -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 数据库的连接
```python
db = pymysql.connect(host, user, password, port, database, charset)
```
port 默认 3306

charset 配置与不配置，字符串编码都是 utf-8

## 数据库的游标对象
通过 cursor 方法创建一个游标对象，使用游标对象的 execute 方法执行 SQL 语句

```python
db = pymysql.connect(......)
cursor = db.cursor()
cursor.execute(......)
```

## 数据库的查询
fetcheone 方法获取下一个查询结果集，fetchall 方法获取全部的返回结果行

## 数据库的事务
commit 方法提交事务，rollback 方法回滚事务