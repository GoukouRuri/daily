## 默认情况下mysql使用3306端口, 并且允许本地访问

--- 

  - 修改mysql权限
  
```shell
mysql -uroot -p123456
use mysql
update user set host = '%' where user = 'root' and host='localhost';
grant all privileges on *.* to 'root'@'%' identified by '你设置的密码' WITH GRANT OPTION; 
FLUSH PRIVILEGES;
重启mysql
```

  - 查看3306监听状况
  
```shell
`netstat -an | grep 3306` 
```
  - 修改mysql的配置
  
```shell
# 查看mysql使用的my.cnf，最前面优先级最高
mysql --help | grep my.cnf

# 打开my.cnf, 修改bind_address为bind-address = 0.0.0.0
vim /etc/my.cnf
改完重启iptables
```
- 出现`2003-can't connect to mysql server on ' ' (10038)`这个报错

  - 修改防火墙规则,允许3306端口对外访问 
  - 检查云平台安全组是否开启3306端口入方向，没有则添加
  
```shell
$ vi /etc/sysconfig/iptables
```

在80下方添加规则`-A INPUT -p tcp -m state --state NEW -m tcp --dport 3306 -j ACCEPT`

重启防火墙
