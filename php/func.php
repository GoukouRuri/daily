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


# 常量
define("AAA", '123'); // 定义一个常量
constant("AAA");    // 获取常量的值
defined("AAA");    // 检查常量是否定义或者存在 返回true或false 


# 格式化字符串写入变量中
$number = 9;
$str = "Beijing";
$txt = vsprintf("There are %u million bicycles in %s.", array($number,$str));
$txt = sprintf("There are %u million bicycles in %s.", $number, $str);
$txt = printf("There are %u million bicycles in %s.", $number, $str);


# 把变量格式化输出到文本文件中 (不常用)
$number = 9;
$str = "Beijing";
$file = fopen("test.txt","w");
echo fprintf($file,"There are %u million bicycles in %s.",$number,$str); // 返回40(字符数)
echo vfprintf($file,"There are %u million bicycles in %s.",array($number,$str));  // 返回40(字符数)

# 字母大小写转换
// 把每个单词的首字符转换为大写
echo ucwords("hello world");  // Hello World!
// 把字符串中的首字符转换为大写
echo ucfirst("hello world!"); // Hello world!
// 把字符串中的首字符转换为小写
echo lcfirst("Hello world!"); // hello world!
// 把所有字符转换为大写
echo strtoupper("Hello WORLD!"); // HELLO WORLD
// 把所有字符转换为小写
echo strtolower("Hello WORLD!"); // hello world

# 字符串过滤函数
// 从字符串的两端删除空白字符和其他预定义字符,第二参数不传默认去除两端空白字符. 
$str = " Hello World! ";
echo trim($str);  
// 从字符串左侧删除空白字符和其他预定义字符,第二参数不传默认去除两端空白字符. 
$str = " Hello World! ";
echo ltrim($str);  
// 从字符串右侧删除空白字符和其他预定义字符,第二参数不传默认去除两端空白字符. 
$str = " Hello World! ";
echo rtrim($str); 
// 剥去字符串中的 HTML、XML 以及 PHP 的标签, 包括注释, 如果要保留某些标签, 只需要将多个标签用空格分隔后写到strip_tags的第二个参数中
$str = "Hello <b>world!</b>";
echo strip_tags($str);


















