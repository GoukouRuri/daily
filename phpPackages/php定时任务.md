> ### 关于php 自动/定时 执行函数 （将api中的数据每隔一定时间录入数据库）
```php
<?php
function add() {
    // 执行自己写的操作
}

ignore_user_abort(); // 后台运行
set_time_limit(0); // 取消脚本运行时间的超时上限
$interval=60*10;// 每隔半小时运行，这个间隔时间是可以随着 需要进行修改
do{
    add();        //执行的代码
    sleep($interval); // 休眠半小时
}while(true);
```

然后在php的cli模式下执行，即命令行执行php test.php


> ### 使用linux的crontab自动化任务
- touch crontab_1hour_sh
- chmod 755 crontab_1hour_sh
  
  - crontab_1hour_sh中代码(如果是windows下编写上传到linux服务器器下会有编码问题,最好在linux环境下编写)
  ```shell
  #!/bin/bash
  . /etc/profile
  sh -c 'cd /data/wwwroot/default/yuqing;php index.php /Home/KeyWord/index;'
  ```
- crontab -e

  `*/1 * * * *  bash /usr/local/src/crontabs/crontab_timer_1hour.sh`  每分钟执行一次(默认只有root用户可以执行)
  
- 重启crontab服务(不一定必须)
  
  `service crond restart`
  
- 查看日志

  `crontab -l`
  `tail -f 10 /var/log/cron`














