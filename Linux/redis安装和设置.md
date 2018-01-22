## redis配置认证密码[参考资料：https://www.cnblogs.com/langtianya/p/5189234.html]

```conf
/etc/redis.conf
修改requirepass youpassword
修改bind 127.0.0.1       #然后把127.0.0.1改成你允许访问你的redis服务器的ip地址，表示只允许该ip进行访问

这种情况下，我们在启动redis服务器的时候不能再用:redis-server，改为:redis-server path/redis.conf 即在启动的时候指定需要加载的配置文件,其中path/是你上面修改的redis配置文件所在目录

redis-cli -h yourIp -p yourPort -a youPassword //启动redis客户端，并连接服务器
key * 
```












