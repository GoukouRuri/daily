<?php

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

// 第二种 fread(int $handle , int $length) 从 handle 指向的文件中读取最多 length 个字节
$handle = fopen('http://www.baidu.com', 'r');
$content = '';
// 如果所要读取的文件不是本地普通文件,而是远程文件或者流文件,fread不能获得这些文件的大小,需要通过feof()判断是否已经读取到了文件的末尾, 最大可下载大小受php.ini里的memory_limit限制
while(!feof($handle)){
	// 一次不能读取太多 需要切片读取
    $content .= fread($handle, 2000);
}
echo $content;
fclose($handle);

// 第三种 readfile()
// 读取的文件过大,不会报错,但是文件无法下载完整,受php.ini中memory_limit限制
set_time_limit(0);
ini_set('memory_limit', '512M');  // 临时设置最大512M 脚本结束后恢复原设置
ob_start();
header('Content-Type: application/octet-stream');
header('Content-Disposition: attachment; filename='.basename($file));
header('Content-Transfer-Encoding: binary');
readfile($file);
ob_end_clean();

// 其他不常用的文件读取方式
fgetss();
file();
fpassthru();