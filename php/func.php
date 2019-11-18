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


# 字符串搜索函数
// (区分大小写) 查找 "php" 在字符串中第一次出现的位置, 如果没有找到字符串则返回 FALSE, 第二个参数必须为字符串
if (strpos("I like php!", "php") === false) {
	echo "No php";
}

// (不区分大小写) 查找 "php" 在字符串中第一次出现的位置, 如果没有找到字符串则返回 FALSE, 第二个参数必须为字符串
if (stripos("I like php!", "php") === false) {
	echo "No php";
}

// (区分大小写) 查找 "php" 在字符串中最后一次出现的位置, 如果没有找到字符串则返回 FALSE, 第二个参数必须为字符串
if (strrpos("I like php!", "php") === false) {
	echo "No php";
}

// (区分大小写) 查找 "php" 在字符串中最后一次出现的位置, 如果没有找到字符串则返回 FALSE, 第二个参数必须为字符串
if (strripos("I like php!", "php") === false) {
	echo "No php";
}


# 字符串转义和替换函数
// addcslashes 在指定字符前添加反斜杠, 区分大小写, 对以下字符应用 addcslashes() 时请小心：0（NULL）, r（回车）, n（换行）, f 换页）、t（制表符）以及 v（垂直制表符）, 在 PHP 中，\0, \r, \n, \t, \f 以及 \v 是预定义的转义序列
$str = addcslashes('Shanghai is the "biggest" city in China.', '"');  
echo($str);    // Shanghai \is the \"biggest\" city in China.

// addslashes 在预定义字符之前添加反斜杠的字符串, 预定义字符是单引号、双引号、反斜杠、NULL.
$str = addslashes('Shanghai \is the "biggest" city in China.');
echo($str);   // Shanghai \\is the \"biggest\" city in China.

// str_replace 区分大小写, 不支持正则, 作用是将字符串替换成另外一个字符串. 多个要替换的值可以在第一个参数中使用数组, 第四个为可选参数,可以统计替换的次数, 不区分大小写用str_ireplace()
$str = str_replace(array('\\', '"'), '', 'Shanghai \is the "biggest" city in China.');
echo($str);   // Shanghai is the biggest city in China.  将反斜杠和双引号去除

// substr_replace 将某个字符串的一部分替换成另外一个字符串或者在字符串某一部位插入另外一个字符串. 多个字符串需要替换时第一个参数为数组形式, 第三个参数代表起始位置,默认0, 第四个参数为替换长度, 默认是与字符串长度相同, 0代表是插入
$str = substr_replace('Shanghai \is the "biggest" city in China.', 'good', 9);
echo($str);  // Shanghai good  第四个参数没有, 此时为替换
$str = substr_replace('Shanghai \is the "biggest" city in China.', 'good', 9, 0);
echo($str);  // Shanghai good\is the "biggest" city in China. 第四个参数为0, 此时为插入

// 字符串长度函数 针对内码是Utf-8情况
echo strlen("Hello World哈哈哈");  // 一个汉字3个字节, 返回字符串字节数, 并不能得到我们需要的字符串长度的真实值
echo mb_strlen("Hello World哈哈哈"); // 一个汉字1个字节, 返回字符串字节数, 可以更好反馈字符串长度

# 正则匹配搜索函数 preg_match
// 查找文本字符串"php", 模式分隔符后的"i"标记这是一个大小写不敏感的搜索
if (preg_match("/php/i", "PHP is the web scripting language of choice.")) {
    echo "查找到匹配的字符串 php。";
} else {
    echo "未发现匹配的字符串 php。";
} // 执行结果: 查找到匹配的字符串 php

// 查找单词”web“, 模式中的\b标记一个单词边界. 所以只有独立的单词"web"会被匹配,而不会匹配单词的部分内容,比如"webbing" 或 "cobweb"
if (preg_match("/\bweb\b/i", "PHP is the web scripting language of choice.")) {
    echo "查找到匹配的字符串";
} else {
    echo "未发现匹配的字符串";
} // 执行结果: 查找到匹配的字符串
if (preg_match("/\bweb\b/i", "PHP is the website scripting language of choice.")) {
    echo "查找到匹配的字符串";
} else {
    echo "未发现匹配的字符串";
} // 执行结果: 未发现匹配的字符串



















