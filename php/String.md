## string

#### 字符串定义和初始化

* PHP字符串是字节序列,是二进制安全的，也就是说字符串中可以包含null。PHP字符串的大小只受内存限制，通常情况下，PHP字符串都是ASCII，如果要处理一些额外的字符（例如UTF-8编码字符），需要进一步扩展。PHP中字符串的定义方式通常有三种：单引号、双引号、heredocs 下面是PHP初始化字符串的三种方式。

  ```
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

  ```
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
 ```
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
    ```
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
    ```
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
    ```
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

    ```
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

    ```
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

    ```
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

    ```
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

    ```
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

    ```
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

    ```
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
