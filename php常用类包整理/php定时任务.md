> ### 关于php 自动/定时 执行函数 （将api中的数据每隔一定时间录入数据库）
```php
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