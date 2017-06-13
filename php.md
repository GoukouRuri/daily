## string

#### 字符串定义和初始化

* PHP字符串是字节序列,是二进制安全的，也就是说字符串中可以包含null。PHP字符串的大小只受内存限制，通常情况下，PHP字符串都是ASCII，如果要处理一些额外的字符（例如UTF-8编码字符），需要进一步扩展。PHP中字符串的定义方式通常有三种：单引号、双引号、heredocs 下面是PHP初始化字符串的三种方式。

  `$s1='I have gone to the store.';

   $s2="I have gone to the store.";

   $s3=<<<END

   I have gone to the store.

   Would you pay some money for tap water?

   END;`
