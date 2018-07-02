### Mysql5.7的常见问题

------

##### timestamp字段在5.6以上版本如何设置?

explicit_defaults_for_timestamp参数在MySQL 5.6.6开始加入 ，在/etc/my.cnf配置文件中添加或修改为explicit_defaults_for_timestamp=1，然后timestamp类型的字段设置如下：

```mysql
ALTER TABLE `user` add `update_time` timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间';
ALTER TABLE `user` add `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间';
```

[参考资料](http://www.ywnds.com/?p=8309)