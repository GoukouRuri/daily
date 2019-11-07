<?php
// 常用内置函数

# 返回当前 Unix 时间戳和微秒数
$time = microtime(true); // 1376983061.08845800

# 获取程序执行时间
$start = microtime(true);
$end = microtime(true);
echo number_format($end - $start, 10, '.', '')." seconds"; // 保留十位小数 格式化输出时间差


# 函数基于以微秒计的当前时间，生成一个唯一的 ID 
$unique_key = uniqid();  // 5dc370092b263  (高并发和循环条件下会产生重复id)
$unique_key = uniqid(md5(microtime(true)),true)  // 高并发和循环条件下也不会生成重复id
$session_key = session_create_id(); // php7.1以上新增生成session id的函数 高并发也不重复



