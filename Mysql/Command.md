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


-------------------------------------------------
-- 用户表user 
-------------------------------------------------
create table if not exists `user` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `username` VARCHAR(20) NOT NULL COMMENT '用户名',
    `nickname` VARCHAR(20) NOT NULL COMMENT '昵称',
    `password` VARCHAR(100) NOT NULL DEFAULT '000000' COMMENT '密码',
    `status` TINYINT NOT NULL DEFAULT 1 COMMENT '账号状态',
    `email` VARCHAR(50) NOT NULL DEFAULT '' COMMENT '电子邮箱',
    `is_admin` TINYINT NOT NULL DEFAULT 0 COMMENT '是否为管理员(0否 1是)',
    `phone` VARCHAR(11) NOT NULL DEFAULT '' COMMENT '手机号码',
    `fixed_telephone` VARCHAR(20) NOT NULL DEFAULT '' COMMENT '固定电话',
    `avatar` VARCHAR(200) NOT NULL DEFAULT '' COMMENT '用户头像',
    `wechat_openid` VARCHAR(150) NOT NULL DEFAULT '' COMMENT '微信openid',
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8 COMMENT '用户表';
```

