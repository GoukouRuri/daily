> ###### 检查sql语法是否正确

> ###### 通用查询日志

> ###### [explain调试](http://www.cnblogs.com/wangkongming/p/4127902.html)
  
  - explain
  - expalin extended
  
> ###### 锁和事务
  
  - show processlist
  - show status
  - show variables like "%timeout%"
  - 表索,行锁,页锁，元数据锁
  - 启动事务
    
    - start transaction
    - begin
  - 提交事务
   
    - commit
  - 回滚事务
    
    - roolback
  - show engine innodb status
  - 死锁

> 并发问题

  - 在隔离的单线程环境下确认sql是否调优
  - InnoDB监控器
  - 资源占用引起的并发
  
