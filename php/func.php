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

# 文件的写入
$str = "Hello";  // 可以是字符串、数组或数据流
$file = 'test.txt';

// 向文件追加写入内容, 如果文件不存在, 则创建一个新文件.
// 使用 FILE_APPEND 标记, 可以在文件末尾追加内容, 不加则会清空文件原有内容写入.
// LOCK_EX 标记可以加文件写入锁防止多人同时写入, 之后会自动释放锁.
file_put_contents($file, $str, FILE_APPEND | LOCK_EX);     // 成功返回文件字符数, 失败返回false

// fwrite配合fopen进行写入操作
// fopen第二个参数有多种模式  r可读不可写 r+可读可写  w可写不可读 w+可读可写 a可写不可读  a+可读可写
$str = "Hello";  
$file = 'test.txt';
$fp = fopen($file, "w");
$len = fwrite($file, $str);
fclose($fp);

// a和a+模式下指针指向文件末尾 w和w+模式下指针指向文件顶部  因此a模式下是追加式写入  w模式会覆盖原内容写入
$str = "Hello";  
$file = 'test.txt';
$fp = fopen($file, "a");
$len = fwrite($file, $str);
fclose($fp);

// 手动加文件锁和释放锁  
// LOCK_SH  取得共享锁定（读取的程序） LOCK_EX  取得独占锁定（写入的程序） LOCK_UN  释放锁定（无论共享或独占）
$fp = fopen($file, "w+");
if (flock($fp , LOCK_EX)) {
	// 是否有写入锁 没有则我获取独占权限 并加上写入锁 开始写入文件
	echo "我可以写入";
	fwrite($fp, $str);

	// 释放锁
	flock($fp, LOCK_UN);
} else {
	echo "有人加了锁, 我不能写入";
}
fclose($fp);


# 文件的读取

// 第一种 file_get_contents (推荐性能比其他方式好)
$file = "test.txt";
if (file_exists($file)) {
	// 如果文件存在
	$str = file_get_contents($file);   // 从文件中读取内容
	$str = str_replace("\r\n", "<br/>", $str);
	echo $str;
}


















