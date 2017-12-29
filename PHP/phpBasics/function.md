> ### 变量与类型相关扩展

* [数组函数](http://php.net/manual/zh/book.array.php)

* [类/对象](http://php.net/manual/zh/book.classobj.php)

* [过滤器函数](http://php.net/manual/zh/book.filter.php)

* [字符类型检测](http://php.net/manual/zh/book.ctype.php)

* [函数处理](http://php.net/manual/zh/book.funchand.php)

* [反射](http://php.net/manual/zh/book.reflection.php)

  - 参考资料(http://www.jb51.net/article/106769.htm)
  
* [变量处理](http://php.net/manual/zh/book.var.php)

> ### 文本处理

* [字符串](http://php.net/manual/zh/ref.strings.php)

      - ## string
        
        #### 字符串定义和初始化
        
        * PHP字符串是字节序列,是二进制安全的，也就是说字符串中可以包含null。PHP字符串的大小只受内存限制，通常情况下，PHP字符串都是ASCII，如果要处理一些额外的字符（例如UTF-8编码字符），需要进一步扩展。PHP中字符串的定义方式通常有三种：单引号、双引号、heredocs 下面是PHP初始化字符串的三种方式。
        
          ```php
           <?php
           $s1='I have gone to the store.';
        
           $s2="I have gone to the store.";
        
           $s3=<<<END
        
           I have gone to the store.
        
           Would you pay some money for tap water?
        
           END;
          ```
        
        #### 访问字符串
        
        * 问题：
        想知道一个字符串中是否包含一个特定的子串。例如，想查看一个email地址中是否包含@。
        解决方案：
        使用strpos()或者strstr()
        
          示例 :
        
          ```php
          <?php
          if(strpos($_POST['email'],'@qq.com')===false){
            print 'There was no @qq.com in the email address!';
          }
          if(strstr($_POST['email'],'@')===false){
              print 'There was no @ in the email address!';
          }
        
          ```
        
          strpos和strstr两者的区别主要是：如果查找失败，则会返回false，如果成功就会返回第一次出现的位置。因为第一次出现的位置可能是0，所以需要使用===来进行判断。strpos查找性能强，但是对中文的支持不好，而strstr相反。
        
          扩展：strpos的有关文档http://www.php.net/strpos
        
        #### 抽取字符串
        
        * 问题：
        希望从字符串中特定的位置开始抽取字符串中的一部分。例如，对于输入的用户名，只希望获取用户名中的前8个字符。
        
          解决方案 : 使用substr()抽取字符串
        
          示例 :
         ```php
         <?php
         //标准格式
         $substring = substr($string,$start,$length);
         //示例
         print substr('watch out for that tree',6,5);
         //输出
         out f
         ```
         扩展：如果$start或者$length为负，具体参考http://www.php.net/substr
        
        #### 替换字符串
        
        * 问题：
        希望用另外一个不同的字符串来替换一个子串。例如，打印一个信用卡号之前，想要对除了后4位以外的部分模糊处理。可以用于显示固定长度的字符串，多出来的部分用省略号替换。
        
            解决方案 :
            使用substr_replace()替换子串
        
            示例 :
            ```php
            <?php
            //标准格式
            $res_str = substr_replace($old_string,$new_string,$start,$length);
            //说明：在old中的start位置开始的length长度用new字符串来替换
            //length=0，表示在start位置插入字符串
            //length不写，表示从start位置开始后面全部截断
        
            //示例
            print substr_replace('My pet is a blue dog.','green',12,4);
            print substr_replace('My pet is a blue dog.','fish.',12);
            print substr_replace('6216 6132 0001 1234 567','...',9);
            //输出
            My pet is a green dog.
            My pet is a fish.
            6216 6132...
            ```
            扩展：如果$start为负，具体参考http://www.php.net/substr-replace
        
        #### 逐字节处理字符串
        
        * 问题：
        需要分别处理字符串中的各个字节
        
            解决方案 :
            使用for循环处理字符串中的各个字节
        
            示例 :
            ```php
            <?php
            //统计字符串中元音字母的个数
            //strstr返回子串第一次出现开始的字符串，例如子串为‘I’，那么返回IOU
            //strpos返回子串第一次出现的位置，例如子串为‘I’，那么返回7
            //strpos的查找性能强，但是对中文的支持不是很好,判断时需要采用!==false
        
            $string = "This weekend, I'm going shopping for a pet chicken.";
            $vowels = 0;
            for($i = 0, $j = strlen($string); $i < $j ; $i++){
              if(strstr('aeiouAEIOU',$string[$i])){
                  $vowels++;
              }
            }
            print $vowels;
            //输出
            14
            ```
            扩展：具体参考http://www.php.net/strstr
        
        #### 按单词或字节反转字符串
        
        * 希望反转一个字符串中的单词或字节
        
            解决方案 :
            使用strrev()按字节反转
        
            示例 :
            ```php
            <?php
            //按字节反转
            print strrev('This is not a palindrome.');
        
            //按单词反转
            $s='Once upon a time there was a turtle.';
            $words=explode(' ',$s);
            $words=array_reverse($words);
            $s=implode(' ',$words);
            print $s;
        
            //输出
            .emordnilap a ton si sihT
            turtle. a was there time a upon Once
            ```
            扩展：具体参考http://www.php.net/strrev 和http://www.php.net/array-reverse
        
        #### 生成随机字符串
        
        * 问题：
        希望生成一个随机字符串
        
            解决方案 :
            使用自定义的str_rand()
        
            示例 :
        
            ```php
            <?php
            //带默认参数的函数
            //mt_rand(min,max)生成随机数包含min和max在内
            function str_rand($length=32,$charset='0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'){
                if(!is_int($length)||$length<0){
                    return false;
                }
                $charset_len=strlen($charset)-1;
                $string='';
                for($i=$length;$i>0;$i--){
                    $string.=$charset[mt_rand(0,$charset_len)];
                }
                return $string;
            }
            print str_rand(16,'.-');
            //输出
            .--..-.-.--.---
            ```
        
        #### 字符串替换
        
        * 问题：
        希望将字符串中空格改为制表符（或者将制表符改为空格），但仍保证文本按制表位对其。例如，用一种统一的格式为用户显示文本。
        
            解决方案 :
            使用str_replace()将空格替换为制表符，或者将制表符替换为空格
        
            示例 :
        
            ```php
            <?php
            //ucfirst()将一个字符串中第一个字母改为大写
            //ucwords()将一个字符串中每一个单词首字母大写
            //strtoupper将字符串的字母全部改为大写
            //strtolower将字符串的字母全部改为小写
        
            print ucfirst("don't play zone defense agaist the 76-ers");
            print ucwords("don't play zone defense agaist the 76-ers");
            print strtoupper("don't play zone defense agaist the 76-ers");
            print strtolower("don't play zone defense agaist the 76-ers");
        
            //输出
            Don't play zone defense agaist the 76-ers
            Don't Play Zone Defense Agaist The 76-ers
            DON'T PLAY ZONE DEFENSE AGAIST THE 76-ERS
            don't play zone defense agaist the 76-ers
            ```
            扩展：具体参考http://www.php.net/str-replace
        
        #### 控制大小写
        
        * 问题：
        希望将字符串中的字母全部改为大小写，或者一部分改为大小写。
        
            解决方案 :
            使用ucfirst(),ucwords(),strtoupper(),strtolower()等来改变。
        
            示例 :
        
            ```php
            <?php
            //ucfirst()将一个字符串中第一个字母改为大写
            //ucwords()将一个字符串中每一个单词首字母大写
            //strtoupper将字符串的字母全部改为大写
            //strtolower将字符串的字母全部改为小写
        
            print ucfirst("don't play zone defense agaist the 76-ers");
            print ucwords("don't play zone defense agaist the 76-ers");
            print strtoupper("don't play zone defense agaist the 76-ers");
            print strtolower("don't play zone defense agaist the 76-ers");
        
            //输出
            Don't play zone defense agaist the 76-ers
            Don't Play Zone Defense Agaist The 76-ers
            DON'T PLAY ZONE DEFENSE AGAIST THE 76-ERS
            don't play zone defense agaist the 76-ers
            ```
            扩展：具体参考http://www.php.net/strtoupper
        
        #### 字符串中的内插函数和表达式
        
        * 问题：
        希望在一个字符串中包含执行某个函数或表达式的结果。
        
            解决方案 :
            使用字符串连接操作符（.）。
        
            示例 :
        
            ```php
            <?php
            //双引号的字符串中可以直接解析变量，对象属性，数组元素等。通常使用{}来分隔。
        
            print "You owe {$amounts['payment']} immediately";
            print "My circle's diameter is ".$circle->getDiameter().' inches';
        
            //输出
            You owe $10 immediately
            My circle's diameter is 10 inches
            ```
        
        #### 去除字符串首尾的空格
        
        * 问题：
        希望从字符串开头和末尾删除空白符。例如在验证用户输入时，可能需要清理数据。
        
            解决方案 :
            使用ltrim(),rtrim(),trim()。ltrime() 函数删除字符串左边的空白符，trim() 函数删除两边的空白符。
        
            示例 :
        
            ```php
            <?php
            //默认的空白符有：换行，回车，空格，水平和垂直制表符以及null
            //需要去除双引号、制表符、空格,可以采用多步实现的方式。
        
            $str="\" <a>penta kill</a>  \"";
            $str=trim($str,'"'); //先去除一些特殊字符
            $str=trim($str);    //单独去除空白字符
            print $str;
        
            //输出
            <a>penta kill</a>
            ```
        
            扩展：具体参考http://www.php.net/trim
        
        #### 生成逗号分隔的数据
        
        * 问题：
        希望将数据格式化为逗号分隔值(CSV)，从而可以由电子表格或者数据库导入。
        
            解决方案 :
            可以使用fputcsv() 函数可以根据一个数据数组生成一个CSV格式的文件行
        
            示例 :
        
            ```php
            <?php
            //示例
            $lists=array( array("aaa","bbb","ccc"),
                          array("111","222","333"),
                          array("A","B"));
            $fp=fopen("file.csv","w");
            //如果要输出到显示器中来,需要使用到一种特殊的输出流 php://output
            //$fp=fopen("php://output","w");
        
            foreach($lists as $flieds){
                //将每一行数据写入到文件中去
                fputcsv($fp,$flieds);
            }
            fclose($fp);
        
            //输出
            aaa,bbb,ccc
            111,222,333
            A,B
            ```
            扩展：具体参考http://www.php.net/fputcsv
        
        #### 解析逗号分隔的数据
        
        * 问题：
        已经有逗号分隔值格式的数据，希望将记录和字段抽取为可以在PHP中处理的一种格式。
        
            解决方案 :
            先用fopen()函数打开文件，使用fgetcsv()读取数据，返回值按照逗号分隔的数组
        
            示例:
        
            ```php
            <?php
            //示例
            $fp=fopen('file.csv','r');
            while($data_line=fgetcsv($fp)){
                for($i=0;$i<cout($data_line);$i++){
                    echo $data_line[$i]." ";
                }
                echo "<br/>";
            }
        
            //输出
            aaa bbb ccc
            111 222 333
            A B
            ```
        
            扩展：具体参考http://www.php.net/fgetcsv
        
        #### 生成固定宽度字段数据记录
        
        * 问题：
        需要格式化数据记录，使得每个字段占据指定数目的字符。
        
            解决方案 :
            使用pack()并提供一个格式字符串，它要指定一个空格填充字符串序列。
        
            示例 :
        
        
            ```
            //示例
            $lists=array( array("aaa","bbb","ccc"),
                          array("111","222","333"));
            foreach($lists as $list ){
                print pack("A3A4A4",$list[0],$list[1],$list[2]);
            }
        
            //输出
            aaa bbb ccc
            111 222 333
            ```
        
            如果需要使用其他字符填充，可以使用substr()来确保字段不会太长，str_pad()来确保字段不会过短。
        
            示例 :
        
        
            ```
            //示例
            $lists=array( array("aaa","bbb","ccc"),
                          array("111","222","333"));
            foreach($lists as $list ){
              $s1=str_pad(substr($list[0],0,5),5,'.');
              $s2=str_pad(substr($list[1],0,5),5,'.');
              $s3=str_pad(substr($list[1],0,5),5,'.');
              print "$s1s2s3\n";
            }
        
            //输出
            aaa..bbb..ccc..
            111..222..333..
            ```
        
            扩展：具体参考http://www.php.net/pack
        
        #### 解析固定宽度字段数据记录
        
        * 问题：
        需要格式化数据记录，使得每个字段占据指定数目的字符。
        
            解决方案 :
            使用substr()或者unpack()函数。
        
            示例 :
        
            //示例
            $binarydata = "AA\0A";
            $array = unpack("c2chars/nint", $binarydata);
            foreach ($array as $key => $value){
                echo "\$array[$key] = $value <br>\n";
            }
        
            //输出
            $array[chars1] = 65
            $array[chars2] = 65
            $array[int] = 65
        
            扩展：具体参考http://www.php.net/unpack
        
        #### 分解字符串
        
        * 问题：
        需要将一个字符串分解为片段。例如，希望访问用户在一个< textarea>表单提交的各行文本。
        
            解决方案 :
            使用explode()或者preg_split()函数。
        
            示例 :
        
            ```
            //explode适用于一些固定的字符分隔的字符串
            //preg_split适用于多种字符分隔的字符串
        
            $words = explode(',','My,sentens,is,not,very,complicated');
            $lines = preg_split('/x/i','31 inches x 22 inches X 9 inches');
            print $words;
            print $lines;
        
            //输出
            My sentens is not very complicated
            31 inches  22 inches  9 inches
            ```
            扩展：具体参考http://www.php.net/explode
        
        #### 使文本在指定行长自动换行
        
        * 问题：
        需要实现字符串自动换行。例如，希望使用< pre>标记显示文本，但是要求不能出现水平滚动条。
        
            解决方案 :
            使用wordwrap()函数。
        
            示例 :
        
            ```
            //wordwrap 默认75个字符换行，默认保留单词的完整性
            $str="Four score and seven years";
            print wordwrap($str,9,"\n\n");//设置9个字符换行
        
            //输出
            Four score
        
            and seven
        
            years
            ```
            扩展：具体参考http://www.php.net/wordwrap
        
        #### 加入或者去除反斜杠
        
        * 问题：有时需要对字符进行自动转义，比如sql语句中addcslashes（string str, stringcharlist）：第1个参数str为待操作的原始字符串，第2个参数charlist说明需要在原始串的哪些字符前加上字符‘\’。
        
        stripcslashes（string str）：去掉字符串中的‘\’。
        
        示例 :
        
            <?php
            $init_str ="select * from Books where name = 'php手册'";
            echo$init_str."#<br>";
            $new_str =addcslashes($init_str,"'");  //在单引号前加反斜杠
            echo $new_str."#<br>";
            $init_str2= stripcslashes($new_str);
            echo $init_str2."#<br>";
            ?>
        
        
        #### 转义HTML标签,过滤标签
        
        * 问题：为了安全问题有时需要转义或者过滤html和javascript标签
        
            常用函数 :
        
            htmlspecialchars   一些常用的HTML元素转换为显示字符串。
            htmlentities   HTML元素转换为显示字符串。
            html_entity_decode  把显示字符串转化为HTML元素。
            strip_tags  剥去字符串中的html,xml,javascript以及php的标签


* [正则表达式(兼容 Perl)](http://php.net/manual/zh/book.pcre.php)

  - [PCRE模式](http://php.net/manual/zh/pcre.pattern.php)
  - [PCRE 函数](http://php.net/manual/zh/ref.pcre.php)
  
> ### 数据库扩展

* 数据库抽象层

  - [PDO](http://php.net/manual/zh/book.pdo.php)

* [针对各数据库系统对应的扩展](http://php.net/manual/zh/refs.database.php)

> ### 日期与时间相关扩展

  - [日期和时间](http://php.net/manual/zh/book.datetime.php)
  
> ### 文件系统相关扩展

  - [目录函数](http://php.net/manual/zh/book.dir.php)
  - [文件信息函数](http://php.net/manual/zh/book.fileinfo.php)
  - [文件系统](http://php.net/manual/zh/book.filesystem.php)
  
> ### 图像生成和处理

  - [GD库和相关函数](http://php.net/manual/zh/book.image.php)
    
    - 范例
      
      - [使用php创建png图像](http://php.net/manual/zh/image.examples-png.php)
      - [使用 Alpha 通道为图像加水印](http://php.net/manual/zh/image.examples-watermark.php)
      - [使用 imagecopymerge() 函数创建半透明水印](http://php.net/manual/zh/image.examples.merged-watermark.php)
      
    - [GD和图像处理函数](http://php.net/manual/zh/ref.image.php)
    - Gmagick
    - [ImageMagick](http://php.net/manual/zh/refs.utilspec.image.php)
    
> ### [匿名函数](http://php.net/manual/zh/functions.anonymous.php)

  >匿名函数（Anonymous functions），也叫闭包函数（closures），允许 临时创建一个没有指定名称的函数。最经常用作回调函数（callback）参数的值。
   匿名函数目前是通过 Closure 类来实现的
   
   - Note: 可以在闭包中使用 func_num_args()，func_get_arg() 和 func_get_args()
   ```php
    <?php
    // 一个基本的购物车，包括一些已经添加的商品和每种商品的数量。
    // 其中有一个方法用来计算购物车中所有商品的总价格，该方法使
    // 用了一个 closure 作为回调函数。
    class Cart
    {
        const PRICE_BUTTER  = 1.00;
        const PRICE_MILK    = 3.00;
        const PRICE_EGGS    = 6.95;
    
        protected   $products = array();
        
        public function add($product, $quantity)
        {
            $this->products[$product] = $quantity;
        }
        
        public function getQuantity($product)
        {
            return isset($this->products[$product]) ? $this->products[$product] :
                   FALSE;
        }
        
        public function getTotal($tax)
        {
            $total = 0.00;
            
            $callback =
                function ($quantity, $product) use ($tax, &$total)
                {
                    $pricePerItem = constant(__CLASS__ . "::PRICE_" .
                        strtoupper($product));
                    $total += ($pricePerItem * $quantity) * ($tax + 1.0);
                };
            
            array_walk($this->products, $callback);
            return round($total, 2);;
        }
    }
    
    $my_cart = new Cart;
    
    // 往购物车里添加条目
    $my_cart->add('butter', 1);
    $my_cart->add('milk', 3);
    $my_cart->add('eggs', 6);
    
    // 打出出总价格，其中有 5% 的销售税.
    print $my_cart->getTotal(0.05) . "\n";
    // 最后结果是 54.29
    ?>
   ```
> ### 对象相关的函数
  
###### [属性](http://php.net/manual/zh/language.oop5.properties.php)

  - 类的变量成员叫做"属性"，或者叫"字段"、"特征"，在本文档统一称为"属性"。属性声明是由关键字 public，protected 或者 private 开头，然后跟一个普通的变量声明来组成。属性中的变量可以初始化，但是初始化的值必须是常数，这里的常数是指 PHP 脚本在编译阶段时就可以得到其值，而不依赖于运行时的信息才能求值。
  
###### [类常量](http://php.net/manual/zh/language.oop5.constants.php)

  - 可以把在类中始终保持不变的值定义为常量。在定义和使用常量的时候不需要使用 $ 符号。
    
    常量的值必须是一个定值，不能是变量，类属性，数学运算的结果或函数调用。

###### [自动加载](http://php.net/manual/zh/language.oop5.autoload.php)

  -  spl_autoload_register() 函数可以注册任意数量的自动加载器，当使用尚未被定义的类（class）和接口（interface）时自动去加载。通过注册自动加载器，脚本引擎在 PHP 出错失败前有了最后一个机会加载所需的类。

###### [构造函数和析构函数](http://php.net/manual/zh/language.oop5.decon.php)

  - 如果子类中定义了构造函数则不会隐式调用其父类的构造函数。要执行父类的构造函数，需要在子类的构造函数中调用 parent::__construct()。如果子类没有定义构造函数则会如同一个普通的类方法一样从父类继承（假如没有被定义为 private 的话）
  
###### [访问控制](http://php.net/manual/zh/language.oop5.visibility.php)(修饰符)

  - 对属性或方法的访问控制，是通过在前面添加关键字 public（公有），protected（受保护）或 private（私有）来实现的。被定义为公有的类成员可以在任何地方被访问。被定义为受保护的类成员则可以被其自身以及其子类和父类访问。被定义为私有的类成员则只能被其定义所在的类访问。
  - public 表示全局，类内部外部子类都可以访问；
  - private表示私有的，只有本类内部可以使用,不可以被子类继承；
  - protected表示受保护的，只有本类或子类或父类中可以访问；
  
###### [对象继承](http://php.net/manual/zh/language.oop5.inheritance.php)

  - final 类不可被继承
  
###### [范围解析操作符](http://php.net/manual/zh/language.oop5.paamayim-nekudotayim.php)(::)

  - 范围解析操作符（也可称作 Paamayim Nekudotayim）或者更简单地说是一对冒号，可以用于访问静态成员，类常量，还可以用于覆盖类中的属性和方法。
  - self，parent 和 static 这三个特殊的关键字是用于在类定义的内部对其属性或方法进行访问的。
  
###### [静态关键字static](http://php.net/manual/zh/language.oop5.static.php)

  - static 关键字来定义静态方法和属性
  
###### [抽象类](http://php.net/manual/zh/language.oop5.abstract.php)和[接口](http://php.net/manual/zh/language.oop5.interfaces.php)

  - 参考资料
    
    - http://www.jb51.net/article/81641.htm
    - http://www.imooc.com/article/13925?block_id=tuijian_wz

###### [Trait](http://php.net/manual/zh/language.oop5.traits.php)

  - 参考资料
  
    - http://oomusou.io/php/php-trait/
 
###### [匿名类](http://php.net/manual/zh/language.oop5.anonymous.php)

###### [方法重载](http://php.net/manual/zh/language.oop5.overloading.php)

###### [遍历对象](http://php.net/manual/zh/language.oop5.iterations.php)
  
  - PHP 5 提供了一种定义对象的方法使其可以通过单元列表来遍历，例如用 foreach 语句。默认情况下，所有可见属性都将被用于遍历。
  
###### [魔术方法](http://php.net/manual/zh/language.oop5.magic.php)

  - __sleep()和__wakeup()
  
###### [Final 关键字](http://php.net/manual/zh/language.oop5.final.php)

  - PHP 5 新增了一个 final 关键字。如果父类中的方法被声明为 final，则子类无法覆盖该方法。如果一个类被声明为 final，则不能被继承。 

###### [对象复制clone](http://php.net/manual/zh/language.oop5.cloning.php)

  - 参考资料
  
    - http://itopic.org/php-clone.html
    
###### [对象比较](http://php.net/manual/zh/language.oop5.object-comparison.php)

###### [类型约束](http://php.net/manual/zh/language.oop5.typehinting.php)

  - PHP 5 可以使用类型约束。函数的参数可以指定必须为对象（在函数原型里面指定类的名字），接口，数组（PHP 5.1 起）或者 callable（PHP 5.4 起）。不过如果使用 NULL 作为参数的默认值，那么在调用函数的时候依然可以使用 NULL 作为实参。
  - 如果一个类或接口指定了类型约束，则其所有的子类或实现也都如此。
  - 类型约束不能用于标量类型如 int 或 string。Traits 也不允许。

###### [后期静态绑定](http://php.net/manual/zh/language.oop5.late-static-bindings.php)

###### [对象和引用](http://php.net/manual/zh/language.oop5.references.php)

  - PHP 的引用是别名，就是两个不同的变量名字指向相同的内容。在 PHP 5，一个对象变量已经不再保存整个对象的值。只是保存一个标识符来访问真正的对象内容。 当对象作为参数传递，作为结果返回，或者赋值给另外一个变量，另外一个变量跟原来的不是引用的关系，只是他们都保存着同一个标识符的拷贝，这个标识符指向同一个对象的真正内容。

###### [对象和序列化](http://php.net/manual/zh/language.oop5.serialization.php)
 
  













  
  
  
  
  
  
  
  
  
  
  
  
  
  
    
