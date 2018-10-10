## Personal Daily Note

#### writed by GoukouRuri

[![Build Status](https://travis-ci.org/laravel/framework.svg)](https://travis-ci.org/laravel/framework)
[![Total Downloads](https://poser.pugx.org/laravel/framework/d/total.svg)](https://packagist.org/packages/laravel/framework)
[![Latest Stable Version](https://poser.pugx.org/laravel/framework/v/stable.svg)](https://packagist.org/packages/laravel/framework)
[![Latest Unstable Version](https://poser.pugx.org/laravel/framework/v/unstable.svg)](https://packagist.org/packages/laravel/framework)
[![License](https://poser.pugx.org/laravel/framework/license.svg)](https://packagist.org/packages/laravel/framework)

> 一个php技术栈后端猿的知识储备大纲

## 前言

主要是php, mysql方面知识点   -- writed at 2017.6.14

## 备注

| 状态      | 含义                     |
| --------- | ------------------------ |
| not-start | 当前未开始总结           |
| doing     | 总结中                   |
| α         | 目前仅供参考未修正和发布 |
| done      | 总结完毕                 |
| fixing    | 查漏补缺修改中           |

### 官方文档(doing)

- 符合PSR的PHP编程规范(含部分个人建议)
  - [实例](https://github.com/TIGERB/easy-tips/blob/master/php/standard.php)
  - [文档](https://github.com/TIGERB/easy-tips/blob/master/php/standard.md)
- 基础知识[读(R)好(T)文(F)档(M)]
  - [数据类型](http://php.net/manual/zh/language.types.php)
  - [运算符优先级](http://php.net/manual/zh/language.operators.precedence.php)
  - [string函数](http://php.net/ref.strings.php)
  - [array函数](http://php.net/manual/zh/ref.array.php)
  - [math函数](http://php.net/manual/zh/ref.math.php)
  - [面向对象](http://php.net/manual/zh/language.oop5.php)
  - 版本新特性
    - [7.1](http://php.net/manual/zh/migration71.new-features.php)
    - [7.0](http://php.net/manual/zh/migration70.new-features.php)
    - [5.6](http://php.net/manual/zh/migration56.new-features.php)
    - [5.5](http://php.net/manual/zh/migration55.new-features.php)
    - [5.4](http://php.net/manual/zh/migration54.new-features.php)
    - [5.3](http://php.net/manual/zh/migration53.new-features.php)

### PHP部分

------

##### 数组排序

```
sort() - 以升序对数组排序(数字或者字母升序)
rsort() - 以降序对数组排序(数字或者字母升序)
asort() - 根据值，以升序对关联数组进行排序
ksort() - 根据键，以升序对关联数组进行排序
arsort() - 根据值，以降序对关联数组进行排序
krsort() - 根据键，以降序对关联数组进行排序
```



##### 超全局变量

```
$GLOBALS
$_SERVER
$_REQUEST
$_POST
$_GET
$_FILES
$_ENV
$_COOKIE
$_SESSION
```



##### 日期时间

```
date(format,timestamp)        //第二个参数可选，默认当前时间

mktime() //返回日期的 Unix 时间戳
mktime(hour,minute,second,month,day,year)

strtotime() 函数用于把人类可读的字符串转换为 Unix 时间
```



##### include和require的区别

```
include如果引入的文件不存在,试图继续往下执行,报一个warning
而require如果引入的文件不存在,报fatal error,不再继续执行.

_once 会自动判断文件是否已经引入,如果引入,不再重复执行.
即:保证被包含文件只可能被引入一次.
(如果包含的文件里有定义函数，那么被包含的文件只能被包含一次，如果多次包含，就会出现函数重定义的错误，php是不运行函数重定义的，会出现致命错误，之后代码不在运行)

有的文件不允许被包含多次? 可以用_once来控制,但是,如果从文件的设计上,比较规范,能保证肯定不会出现多次包含的错误,这种情况下 建议用include,因为include_once要检测之前有没有包含,效率没有include高
```



##### 读取文件

readfile() 函数读取文件，并把它写入输出缓冲。

```php
<?php
echo readfile("webdictionary.txt");
?>
```

打开文件的更好的方法是通过 fopen() 函数。此函数为您提供比 readfile() 函数更多的选项。fopen() 的第一个参数包含被打开的文件名，第二个参数规定打开文件的模式。如果 fopen() 函数未能打开指定的文件，下面的例子会生成一段消息

```php
<?php
$myfile = fopen("webdictionary.txt", "r") or die("Unable to open file!");
echo fread($myfile,filesize("webdictionary.txt"));
fclose($myfile);
?>
```

如何逐行读取文件中数据

```php
<?php
$myfile = fopen("webdictionary.txt", "r") or die("Unable to open file!");
// 输出单行直到 end-of-file
while(!feof($myfile)) {
  echo fgets($myfile) . "<br>";
}
fclose($myfile);
?>
```

##### 创建文件

fopen() 函数也用于创建文件。也许有点混乱，但是在 PHP 中，创建文件所用的函数与打开文件的相同。如果您用 fopen() 打开并不存在的文件，此函数会创建文件，假定文件被打开为写入（w）或增加（a）。如果您试图运行这段代码时发生错误，请检查您是否有向硬盘写入信息的 PHP 文件访问权限。

```php
$myfile = fopen("testfile.txt", "w")
```

##### 写入文件

fwrite() 用于写入文件, 第一个参数包含要写入的文件的文件名，第二个参数是被写的字符串。默认会覆盖已有的数据。

```php
<?php
$myfile = fopen("newfile.txt", "w") or die("Unable to open file!");
$txt = "Bill Gates\n";
fwrite($myfile, $txt);
$txt = "Steve Jobs\n";
fwrite($myfile, $txt);
fclose($myfile);
?>
```

##### 数组函数

array_change_key_case()
将数组的所有的键转换为大写字母或小写字母, 如果未提供可选参数（即第二个参数），则默认转换为小写字母。

```php
<?php
$age=array("Bill"=>"60","Steve"=>"56","Mark"=>"31");
print_r(array_change_key_case($age,CASE_UPPER));
?>
```

array_chunk()

把数组分割为按照指定长度分给成多个数组,第三个可选参数是一个布尔值，它指定新数组的元素是否有和原数组相同的键（用于关联数组），还是从 0 开始的新数字键（用于索引数组）。默认是分配新的键。

```php
<?php
$cars=array("Volvo","BMW","Toyota","Honda","Mercedes","Opel");
print_r(array_chunk($cars,2,false));
?>
```

array_column()

从多维数组中取出某一列的值,返回数组形式

```php
<?php
// 表示由数据库返回的可能记录集的数组
$a = array(
  array(
    'id' => 5698,
    'first_name' => 'Bill',
    'last_name' => 'Gates',
  ),
  array(
    'id' => 4767,
    'first_name' => 'Steve',
    'last_name' => 'Jobs',
  ),
  array(
    'id' => 3809,
    'first_name' => 'Mark',
    'last_name' => 'Zuckerberg',
  )
);

$last_names = array_column($a, 'last_name');
print_r($last_names);
?>
```

array_combine()

通过合并两个数组来创建一个新数组，其中的前一个数组元素为键名，后一个数组元素为键值，键名数组和键值数组的元素个数必须相同！

如果其中一个数组为空，或者两个数组的元素个数不同，则该函数返回 false。

```php
<?php
$fname=array("Bill","Steve","Mark");
$age=array("60","56","31");

$c=array_combine($fname,$age);
print_r($c);
?>
```

array_merge()

把两个以上数组合并为一个数组, 如果两个或更多个数组元素有相同的键名，则最后的元素会覆盖其他元素。

```php
<?php
$a1=array("red","green");
$a2=array("blue","yellow");
print_r(array_merge($a1,$a2));
?>
```

array_merge_recursive()

与 [array_merge()](http://www.w3school.com.cn/php/func_array_merge.asp) 函数的区别在于处理两个或更多个数组元素有相同的键名时。array_merge_recursive() 不会进行键名覆盖，而是将多个相同键名的值递归组成一个数组。

```php
<?php
$a1=array("a"=>"red","b"=>"green");
$a2=array("c"=>"blue","b"=>"yellow");
print_r(array_merge_recursive($a1,$a2));
?>
```

array_count_values()

对数组中的所有值进行计数, 返回一个数组，其元素的键名是原数组的值，键值是该值在原数组中出现的次数

```php
<?php
$a=array("A","Cat","Dog","A","Dog");
print_r(array_count_values($a));
?>
```

array_diff()

比较两个数组，并返回差集 , 只比较值

```php
<?php
$a1=array("a"=>"red","b"=>"green","c"=>"blue","d"=>"yellow");
$a2=array("e"=>"red","f"=>"green","g"=>"blue");

$result=array_diff($a1,$a2);
print_r($result);
?>
```

array_diff_key()

比较两个数组，并返回差集 , 只比较键

```php
<?php
$a1=array("a"=>"red","b"=>"green","c"=>"blue");
$a2=array("a"=>"red","c"=>"blue","d"=>"pink");

$result=array_diff_key($a1,$a2);
print_r($result);
?>
```

array_diff_assoc()

比较两个数组，并返回差集 , 同时比较键和值

```php
<?php
$a1=array("a"=>"red","b"=>"green","c"=>"blue","d"=>"yellow");
$a2=array("a"=>"red","b"=>"green","c"=>"blue");

$result=array_diff_assoc($a1,$a2);
print_r($result);
?>
```

array_intersect()

比较两个数组，并返回交集，只比较值

```php
<?php
$a1=array("a"=>"red","b"=>"green","c"=>"blue","d"=>"yellow");
$a2=array("e"=>"red","f"=>"green","g"=>"blue");

$result=array_intersect($a1,$a2);
print_r($result);
?>
```

array_intersect_key()

比较两个数组，并返回交集，只比较键

```php
<?php
$a1=array("a"=>"red","b"=>"green","c"=>"blue");
$a2=array("a"=>"red","c"=>"blue","d"=>"pink");

$result=array_intersect_key($a1,$a2);
print_r($result);
?>
```

array_intersect_assoc()

比较两个数组，并返回交集，同时比较键和值

```php
<?php
$a1=array("a"=>"red","b"=>"green","c"=>"blue","d"=>"yellow");
$a2=array("a"=>"red","b"=>"green","c"=>"blue");

$result=array_intersect_assoc($a1,$a2);
print_r($result);
?>
```

array_fill(index, number, value)

用给定的值填充数组，返回的数组有 *number* 个元素，值为 *value*。返回的数组使用数字索引，从 *start* 位置开始并递增。如果 *number* 为 0 或小于 0，就会出错。

```php
<?php
$a1=array_fill(3,4,"blue");
print_r($a1);
?>
```

array_fill_keys()

使用指定的键和值填充数组。

```php
<?php
$keys=array("a","b","c","d");
$a1=array_fill_keys($keys,"blue");
print_r($a1);
?>
```

array_pad()

用值将数组填补到指定长度

```php
<?php
$a=array("red","green");
print_r(array_pad($a,5,"blue"));
?>
```

array_filter()

用回调函数过滤数组中的值。

该函数把输入数组中的每个键值传给回调函数。如果回调函数返回 true，则把输入数组中的当前键值返回结果数组中。数组键名保持不变。

```php
<?php
function test_odd($var)
{
return($var & 1);
}

$a1=array("a","b",2,3,4);
print_r(array_filter($a1,"test_odd"));
?>
```

array_flip()

用于反转/交换数组中所有的键名以及它们关联的键值, 如果同一值出现了多次，则最后一个键名将作为它的值，所有其他的键名都将丢失。

如果原数组中的值的数据类型不是字符串或整数，函数将报错。

```php
<?php
$a1=array("a"=>"red","b"=>"green","c"=>"blue","d"=>"yellow");
$result=array_flip($a1);
print_r($result);
?>
```

array_key_exists()

检查数组中是否存在某个键

```php
<?php
$a=array("Volvo"=>"XC90","BMW"=>"X5");
if (array_key_exists("Volvo",$a))
  {
  echo "键存在！";
  }
else
  {
  echo "键不存在！";
  }
?>
```

array_keys()

返回数组中所有的键名

```php
<?php
$a=array("Volvo"=>"XC90","BMW"=>"X5","Toyota"=>"Highlander");
print_r(array_keys($a));
?>
```

array_values()

返回数组中所有的值

```php
<?php
$a=array("Name"=>"Bill","Age"=>"60","Country"=>"USA");
print_r(array_values($a));
?>
```

array_map()

函数将用户自定义函数或者匿名函数作用到数组中的每个值上，并返回用户自定义函数作用后的带有新值的数组。

回调函数接受的参数数目应该和传递给 array_map() 函数的数组数目一致。也可以传入两个数组

```php
<?php
// 单个数组的例子
function myfunction($v)
{
$v=strtoupper($v);
  return $v;
}

$a=array("Animal" => "horse", "Type" => "mammal");
print_r(array_map("myfunction",$a));

//多个数组的例子
function myfunction($v1,$v2)
{
if ($v1===$v2)
  {
  return "same";
  }
return "different";
}

$a1=array("Horse","Dog","Cat");
$a2=array("Cow","Dog","Rat");
print_r(array_map("myfunction",$a1,$a2));
?>
```

array_sum()

计算并返回数组的和

```php
<?php
$a=array(5,15,25);
echo array_sum($a);
?>
```

array_product()

计算并返回数组的乘积

```php
<?php
$a=array(5,5);
echo(array_product($a));
?>
```

array_pop()

删除数组中的最后一个元素, 并返回那个元素(出栈)

```php
<?php
$a=array("red","green","blue");
array_pop($a);
print_r($a);
?>
```

array_push()

在数组末尾插入元素，返回数组长度(入栈)

```php
<?php
$a=array("red","green");
array_push($a,"blue","yellow");
print_r($a);
?>
```

array_shift()

删除数组中的第一个元素, 并返回那个元素

```php
<?php
$a=array("a"=>"red","b"=>"green","c"=>"blue");
echo array_shift($a);
print_r ($a);
?>
```

array_unshift()

在数组开头插入元素，返回数组长度

```php
<?php
$a=array("a"=>"red","b"=>"green");
array_unshift($a,"blue");
print_r($a);
?>

```

array_rand

返回数组中的随机键名，或者如果您规定函数返回不只一个键名，则返回包含随机键名的数组。

```php
<?php
$a=array("red","green","blue","yellow","brown");
$random_keys=array_rand($a,3);
echo $a[$random_keys[0]]."<br>";
echo $a[$random_keys[1]]."<br>";
echo $a[$random_keys[2]];
?>
```

array_replace()

使用第二个数组（a2）的值替换第一个数组（a1）的值

```php
<?php
$a1=array("red","green");
$a2=array("blue","yellow");
print_r(array_replace($a1,$a2));
?>
```

array_reverse()

以相反的元素顺序返回数组

```php
<?php
$a=array("a"=>"Volvo","b"=>"BMW","c"=>"Toyota");
print_r(array_reverse($a));
?>
```

array_search()

在数组中搜索某个值，并返回对应的键名

```php
<?php
$a=array("a"=>"red","b"=>"green","c"=>"blue");
echo array_search("red",$a);
?>
```

array_slice()

对数组进行切片

```php
<?php
$a=array("red","green","blue","yellow","brown");
print_r(array_slice($a,2));
?>
```

array_splice()

从数组中移除选定的元素，并用新元素取代它。该函数也将返回包含被移除元素的数组。

```php
<?php
$a1=array("0"=>"red","1"=>"green");
$a2=array("0"=>"purple","1"=>"orange");
array_splice($a1,1,0,$a2);
print_r($a1);
?>
```

array_unique()

移除数组中的重复的值，并返回结果数组

```php
<?php
$a=array("a"=>"red","b"=>"green","c"=>"red");
print_r(array_unique($a));
?>
```

compact()

创建一个包含变量名和它们的值的数组

```
<?php
$firstname = "Bill";
$lastname = "Gates";
$age = "60";
$result = compact("firstname", "lastname", "age");
print_r($result);
?>

```

range()

该函数返回一个包含从 *low* 到 *high* 之间的元素的数组。

```php
<?php
$number = range(0,5);
print_r ($number);
?>
```

shuffle()

把数组中的元素按随机顺序重新排序：

```php
<?php
$my_array = array("red","green","blue","yellow","purple");

shuffle($my_array);
print_r($my_array);
?>
```

