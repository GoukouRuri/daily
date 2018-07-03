### Mysql5.7 CLI指令集整理

```mysql
# 列出所有数据库
Mysql [(none)] > show databases;

# 列出某个数据库中所有表
Mysql [(none)] > show tables from zoo;

# 列出当前数据库支持的索引情况
Mysql [(none)] > show ENGINES;

# 创建一个库
Mysql [(none)] > CREATE DATABASE zoo;

# 删除数据库
Mysql [(none)] > DROP DATABASE zoo;

# 列出数据库创建语句
Mysql [(none)] > show CREATE DATABASE zoo;

# 切换数据库
Mysql [(none)] > use zoo;

# 查看数据库默认使用的引擎
Mysql [(none)] > show variables like "%storage_engine%";

# 查看数据库相关日志(binlog等)
Mysql [(none)] > show variables like "log%";

# 创建数据表
-------------------------------------------------
-- 用户表user 
-------------------------------------------------
CREATE TABLE IF NOT EXISTS `user` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `username` VARCHAR(20) NOT NULL COMMENT '用户名',
    `nickname` VARCHAR(20) NOT NULL DEFAULT '' COMMENT '昵称',
    `password` VARCHAR(100) NOT NULL DEFAULT '000000' COMMENT '密码',
    `status` TINYINT NOT NULL DEFAULT 1 COMMENT '账号状态',
    `email` VARCHAR(50) NOT NULL DEFAULT '' COMMENT '电子邮箱',
    `is_admin` TINYINT NOT NULL DEFAULT 0 COMMENT '是否为管理员(0否 1是)',
    `phone` VARCHAR(11) NOT NULL DEFAULT '' COMMENT '手机号码',
    `fixed_telephone` VARCHAR(20) NOT NULL DEFAULT '' COMMENT '固定电话',
    `avatar` VARCHAR(200) NOT NULL DEFAULT '' COMMENT '用户头像',
    `wechat_openid` VARCHAR(150) NOT NULL DEFAULT '' COMMENT '微信openid',
    `create_time` DATETIME  NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_time` DATETIME  NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8 COMMENT '用户表';

-------------------------------------------------
-- 用户地址表user_address
-------------------------------------------------
CREATE TABLE IF NOT EXISTS `user_address` (
    `address_id` INT NOT NULL AUTO_INCREMENT,
    `user_id` INT NOT NULL COMMENT '用户id',
    `wechat_openid` VARCHAR(150) NOT NULL DEFAULT '' COMMENT '微信openid',
    `is_default` TINYINT NOT NULL DEFAULT 0 COMMENT '是否设为默认(0否 1是)',
    `province_id` SMALLINT NOT NULL DEFAULT 0 COMMENT '省级id',
    `city_id` SMALLINT NOT NULL DEFAULT 0 COMMENT '市级id',
    `district_id` INT NOT NULL DEFAULT 0 COMMENT '区县级id',
    `address_detail` VARCHAR(200) NOT NULL DEFAULT '' COMMENT '详细地址',
    `is_del` TINYINT NOT NULL DEFAULT 0 COMMENT '是否删除(0否 1是)',
    `create_time` DATETIME  NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_time` DATETIME  NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (`address_id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8 COMMENT '用户地址表';

-------------------------------------------------
-- 公司表company 
-------------------------------------------------
CREATE TABLE IF NOT EXISTS `company` (
    `company_id` INT NOT NULL AUTO_INCREMENT,
    `company_name` VARCHAR(100) NOT NULL DEFAULT '' COMMENT '公司名称',
    `country_id` SMALLINT NOT NULL DEFAULT 0 COMMENT '所在国家id',
    `city_id` INT NOT NULL DEFAULT 0 COMMENT '所在城市id',
    `company_address` VARCHAR(150) NOT NULL DEFAULT '' COMMENT '公司地址',
    `employer_number` INT NOT NULL DEFAULT 0 COMMENT '雇员数量',
    `company_birth` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '公司创立时间',
    `industry` INT NOT NULL DEFAULT 0 COMMENT '行业',
    `is_del` TINYINT NOT NULL DEFAULT 0 COMMENT '是否删除(0否 1是)',
    `create_time` DATETIME  NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_time` DATETIME  NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (`company_id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8 COMMENT '公司表'; 

-------------------------------------------------
-- 用户-公司关联表user_company 
-------------------------------------------------
CREATE TABLE IF NOT EXISTS `user_company` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `user_id` INT NOT NULL COMMENT '',
    `company_id` INT NOT NULL COMMENT '',
    `is_del` TINYINT NOT NULL DEFAULT 0 COMMENT '是否删除(0否 1是)',
    `create_time` DATETIME  NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_time` DATETIME  NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8 COMMENT = '用户-公司关联表';

# 查看建库语句
Mysql [(none)] > show create database zoo;

# 查看建表语句
Mysql [zoo] > show create table user;

# 删除数据表	
drop database;

# 添加字段(不含有完整性约束限制)
ALTER TABLE `user` add `update_time` timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间';
ALTER TABLE `user` add `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间' AFTER `update_time`;
ALTER TABLE `user` add `address_id` INT NOT NULL DEFAULT 0 COMMENT '用户地址id' AFTER `wechat_openid` ;

# 只修改字段数据类型
ALTER TABLE `user` modify `update_time` timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间';

# 修改字段名称和数据类型
ALTER TABLE `user` change `update_time` `updated_at` timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间';

# 删除字段
ALTER TABLE `user` drop `nickname`;

# 修改表名
ALTER TABLE `user` rename `user_new`;

# 修改表使用的引擎
ALTER TABLE `user` engine = MyISAM;

# 添加外键约束(这里是完整约束，级联用cascade)
ALTER TABLE `user` add foreign key(address_id) references user_address(address_id) on delete restrict on update restrict; 

# 移除外键约束
ALTER TABLE `user_address` drop FOREIGN KEY <生成的外键名>;
```

