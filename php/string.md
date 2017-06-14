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
