### Mysql5.7的常见问题

------

##### timestamp字段在5.6以上版本如何设置？

explicit_defaults_for_timestamp参数在MySQL 5.6.6开始加入 ，在/etc/my.cnf配置文件中添加或修改为explicit_defaults_for_timestamp=1，然后timestamp类型的字段设置如下：

```mysql
ALTER TABLE `user` add `update_time` timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间';
ALTER TABLE `user` add `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间';
```

[参考资料](http://www.ywnds.com/?p=8309)

##### mysql有哪些数据类型？

- 数值数据类型：包括整数类型TINYINT， SMAllINT， MEDIUMINT，INT ，BIGINT，浮点小数类型 FLOAT DOUBLE ，定点小数类型DECIMAL
- 日期/时间数据类型：包括YEAR ，TIME ，DATE ，DATETIME和TIMESTAMP
- 字符串数据类型：包括CHAR，VARCHAR，BINARY，VARBINARY，BLOB，TEXT，ENUM和SET

##### varchar和char之间有什么区别？

- char(M)是固定长度字符串，存储上自动填充空格以达到指定长度，检索时自动删除尾部空格。
- varchar(M)是长度可变的字符串，M只是指定最大字节长度，实际长度由保存的字符串本身决定，存储长度为字符串长度+1个字节，检索时保留尾部空格

##### enum(枚举)和set(集合)有什么区别？

​    enum只能存单值，set可存多值，最多可以存64个成员，空字符串也是合法值，比如存兴趣爱好就适合set类型。enum和set都是字符串类型，但是在类部，mysql是以它们的值对应的索引数值存储它们的。

##### mysql的位运算有什么使用场景？

  有限状态标识和有限权限标识时可以使用，[参考资料](https://www.cnblogs.com/heluo/p/3422357.html)