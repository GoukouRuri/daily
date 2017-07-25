> ###### [属性](http://php.net/manual/zh/language.oop5.properties.php)

  - 类的变量成员叫做"属性"，或者叫"字段"、"特征"，在本文档统一称为"属性"。属性声明是由关键字 public，protected 或者 private 开头，然后跟一个普通的变量声明来组成。属性中的变量可以初始化，但是初始化的值必须是常数，这里的常数是指 PHP 脚本在编译阶段时就可以得到其值，而不依赖于运行时的信息才能求值。
  
> ###### [类常量](http://php.net/manual/zh/language.oop5.constants.php)

  - 可以把在类中始终保持不变的值定义为常量。在定义和使用常量的时候不需要使用 $ 符号。
    
    常量的值必须是一个定值，不能是变量，类属性，数学运算的结果或函数调用。

> ###### [自动加载](http://php.net/manual/zh/language.oop5.autoload.php)

  -  spl_autoload_register() 函数可以注册任意数量的自动加载器，当使用尚未被定义的类（class）和接口（interface）时自动去加载。通过注册自动加载器，脚本引擎在 PHP 出错失败前有了最后一个机会加载所需的类。

> ###### [构造函数和析构函数](http://php.net/manual/zh/language.oop5.decon.php)

  - 如果子类中定义了构造函数则不会隐式调用其父类的构造函数。要执行父类的构造函数，需要在子类的构造函数中调用 parent::__construct()。如果子类没有定义构造函数则会如同一个普通的类方法一样从父类继承（假如没有被定义为 private 的话）
  
> ###### [访问控制](http://php.net/manual/zh/language.oop5.visibility.php)(修饰符)

  - 对属性或方法的访问控制，是通过在前面添加关键字 public（公有），protected（受保护）或 private（私有）来实现的。被定义为公有的类成员可以在任何地方被访问。被定义为受保护的类成员则可以被其自身以及其子类和父类访问。被定义为私有的类成员则只能被其定义所在的类访问。
  - public 表示全局，类内部外部子类都可以访问；
  - private表示私有的，只有本类内部可以使用,不可以被子类继承；
  - protected表示受保护的，只有本类或子类或父类中可以访问；
  
> ###### [对象继承](http://php.net/manual/zh/language.oop5.inheritance.php)

  - final 类不可被继承
  
> ###### [范围解析操作符](http://php.net/manual/zh/language.oop5.paamayim-nekudotayim.php)(::)

  - 范围解析操作符（也可称作 Paamayim Nekudotayim）或者更简单地说是一对冒号，可以用于访问静态成员，类常量，还可以用于覆盖类中的属性和方法。
  - self，parent 和 static 这三个特殊的关键字是用于在类定义的内部对其属性或方法进行访问的。
  
> ###### [静态关键字static](http://php.net/manual/zh/language.oop5.static.php)

  - static 关键字来定义静态方法和属性
  
  
  
  
  
  
  
  
  
  
  
  
  