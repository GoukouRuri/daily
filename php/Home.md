### 数据类型

* 四种标量类型： 
  - boolean（布尔型）  
  - integer（整型）  
  - float（浮点型，也称作 double)  
  - string（字符串）  

* 两种复合类型： 
  - array（数组）  
  - object（对象）  

* 最后是两种特殊类型： 
  - resource（资源）  
  - NULL（无类型）  

* 为了确保代码的易读性，本手册还介绍了一些伪类型： 
  - mixed（混合类型）  
  - number（数字类型）  
  - [callback](http://php.net/manual/zh/language.types.callable.php)（回调类型）
     -  在函数中注册有多个回调内容时(如使用 [call_user_func()](http://php.net/manual/zh/function.call-user-func.php) 与 [call_user_func_array()](http://php.net/manual/zh/function.call-user-func-array.php))，如在前一个回调中有未捕获的异常，其后的将不再被调用。

* 以及伪变量 $...
* 如果想查看某个表达式的值和类型，用 var_dump() 函数。  
  
  如果只是想得到一个易读懂的类型的表达方式用于调试，用 gettype() 函数。要查看某个类型，不要用 gettype()，而用 is_type 函数。以下是一些范例：
  ```
  <?php
  $a_bool = TRUE;   // a boolean
  $a_str  = "foo";  // a string
  $a_str2 = 'foo';  // a string
  $an_int = 12;     // an integer
  
  echo gettype($a_bool); // prints out:  boolean
  echo gettype($a_str);  // prints out:  string
  
  // If this is an integer, increment it by four
  if (is_int($an_int)) {
      $an_int += 4;
  }
  
  // If $bool is a string, print it out
  // (does not print out anything)
  if (is_string($a_bool)) {
      echo "String: $a_bool";
  }
  ?> 
  ```
* 注意变量根据其当时的类型在特定场合下会表现出不同的值。更多信息见类型转换的判别。此外，还可以参考 [PHP类型比较表](http://php.net/manual/zh/types.comparisons.php)看不同类型相互比较的例子。
  - 仔细查看表，实际上只有两种处理,empty处理等同于if($x),而is_null等同于isset()
