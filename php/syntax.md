###### 常用的语言结构

  PHP是将函数以string形式传递的。 可以使用任何内置或用户自定义函数，但除了语言结构例如：array()，echo，empty()，eval()，exit()，isset()，list()，print 或 unset()。
***

###### 变量
  
  > 定义：PHP 中的变量用一个美元符号后面跟变量名来表示。变量名是区分大小写的。 
  - 变量默认总是传值赋值。那也就是说，当将一个表达式的值赋予一个变量时，整个原始表达式的值被赋值到目标变量。这意味着，例如，当一个变量的值赋予另外一个变量时，改变其中一个变量的值，将不会影响到另外一个变量。
  - PHP 也提供了另外一种方式给变量赋值：[引用赋值](http://php.net/manual/zh/language.references.php)。
  
  > 变量的范围:即它定义的上下文背景或者作用域
  
  - global 关键字 : 将变量什么为全局变量
  - static 静态变量仅在局部函数域中存在，但当程序执行离开此作用域时，其值并不丢失。
***

###### 常量

  > 可以用 define() 函数来定义常量，在 PHP 5.3.0 以后，可以使用 const 关键字在类定义之外定义常量。一个常量一旦被定义，就不能再改变或者取消定义。 
  
  - 常量只能包含标量数据(boolean, integer, float 和 string)
  - 可以简单的通过指定其名字来取得常量的值，与变量不同，不应该在常量前面加上 $ 符号。如果常量名是动态的，也可以用函数 constant() 来获取常量的值。用 get_defined_constants() 可以获得所有已定义的常量列表。
  - 常量可以不用理会变量的作用域而在任何地方定义和访问
  - 和使用 define() 来定义常量相反的是，使用 const 关键字定义常量必须处于最顶端的作用区域，因为用此方法是在编译时定义的。这就意味着不能在函数内，循环内以及 if 语句之内用 const 来定义常量。 
***

###### [魔术常量](http://php.net/manual/zh/language.constants.predefined.php)

  > 有八个魔术常量它们的值随着它们在代码中的位置改变而改变,这些特殊的常量不区分大小写
  
###### 运算符 
  - instanceof
   
    - 相关: 
      - is_a()
      - getclass()
   - clone
   
###### 流程控制

  - [declare && ticks](http://blog.csdn.net/udefined/article/details/24333333)
    
    实际上可用tick来进行调试，性能测试，实现简单的多任务，或者做一些后台的I/O操作等等。

###### [函数](http://php.net/manual/zh/language.functions.php)

  - 自定义函数
  - 返回值
  - 可变函数
  
###### 类和对象---please go to Object.md
  
   
   
   
   
  