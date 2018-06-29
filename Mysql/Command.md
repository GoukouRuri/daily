### Mysql5.7 CLI指令集整理

```mysql
# 列出所有数据库
Mysql [(none)] > show databases;

# 列出当前数据库支持的索引情况
Mysql [(none)] > show ENGINES;

# 创建一个库
Mysql [(none)] > CREATE DATABASE zoo;

# 列出数据库创建语句
Mysql [(none)] > show CREATE DATABASE zoo;

# 切换数据库
Mysql [(none)] > use zoo;

# 查看数据库默认使用的引擎
Mysql [(none)] > show variables like "%storage_engine%";

# create table if not exists `user` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `username` VARCHAR(20) NOT NULL,
    `password` VARCHAR(100) NOT NULL DEFAULT '000000',
    `status` TINYINT NOT NULL DEFAULT 1,
    `email` TINYINT NOT NULL DEFAULT '',

);


```

