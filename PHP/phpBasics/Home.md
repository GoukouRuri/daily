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
    - Resource 资源类型 
     
     * 资源 resource 
     
       是一种特殊变量，保存了到外部资源的一个引用。资源是通过专门的函数来建立和使用的。所有这些函数及其相应资源类型见[附录](http://php.net/manual/zh/resource.php)。 
     
       参见 [get_resource_type()](http://php.net/manual/zh/function.get-resource-type.php)。 
     
     
     * 转换为资源 
     
       由于资源类型变量保存有为打开文件、数据库连接、图形画布区域等的特殊句柄，因此将其它类型的值转换为资源没有意义。 
     
     
     * 释放资源 
     
       由于 PHP 4 Zend 引擎引进了引用计数系统，可以自动检测到一个资源不再被引用了（和 Java 一样）。这种情况下此资源使用的所有外部资源都会被垃圾回收系统释放。因此，很少需要手工释放内存。 
     
     
     * Note: 持久数据库连接比较特殊，它们不会被垃圾回收系统销毁。参见[数据库永久连接](http://php.net/manual/zh/features.persistent-connections.php)一章。
     
  - NULL（无类型）  

* 为了确保代码的易读性，本手册还介绍了一些伪类型： 
  - mixed（混合类型）  
  - number（数字类型）  
  - [callback](http://php.net/manual/zh/language.types.callable.php)（回调类型）
     -  在函数中注册有多个回调内容时(如使用 [call_user_func()](http://php.net/manual/zh/function.call-user-func.php) 与 [call_user_func_array()](http://php.net/manual/zh/function.call-user-func-array.php))，如在前一个回调中有未捕获的异常，其后的将不再被调用。

* 以及伪变量 $...
* 如果想查看某个表达式的值和类型，用 var_dump() 函数。  
  
  如果只是想得到一个易读懂的类型的表达方式用于调试，用 gettype() 函数。要查看某个类型，不要用 gettype()，而用 is_type 函数。以下是一些范例：
  ```php
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
  
> ### php语言中数据类型在内存中的分配

  - 参考来源
  
    - http://www.cnblogs.com/mo-beifeng/archive/2011/10/08/2201685.html
  - 内存从逻辑上 说大体上是分为4 段，栈空间段、堆空间段、代码段、初始化静态段(数据段)
  
> ### 安全模式---Warning
                本特性已自 PHP 5.3.0 起废弃并将自 PHP 5.4.0 起移除。

  - [保护措施和安全模式](http://php.net/manual/zh/features.safe-mode.php)
