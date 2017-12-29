### 探索sql注入解决方案
> 参考资料
  - stackoverflow上一位大牛的文章https://phpdelusions.net/sql_injection
  - http://blog.csdn.net/hornedreaper1988/article/details/43520257
  - http://blog.csdn.net/xiaoxian8023/article/details/9154063

- 什么SQL注入是？

SQL注入是不适当的格式化查询的利用。

SQL注入问题的根源在于代码和数据的混合。
实际上，我们的SQL查询是一个程序。一个完整的合法程序 - 就像我们熟悉的PHP脚本一样。所以恰巧我们正在动态地创建这个程序，随时添加一些数据。因此，这些数据可能会干扰程序代码，甚至改变程序代码 - 这种改变就是注入本身。


- 如何完美解决

  - 白名单（对特殊字符和关键字的黑名单是永远无法防止的）
  - mysqli_real_escape_string转义输入(并不能完美过滤,编码的漏洞会使输入跳过他们)
  - 使用mysqli和pdo扩展的预处理语句,即prepare statement机制
  



































