### [php五大运行模式](http://www.phpernote.com/news/723.html)
  
  - CGI运行模式
  
  - Fast-CGI运行模式
  
  - CLI运行模式
  
  - ISAPI运行模式
  
  - apache模块的DLL运行模式
  
### 安全
  
  > 绝对安全的系统是不存在的，因此安全业界常用的方法有助于平衡可用性和风险。最好的安全机制应该能在不防碍用户，并且不过多地增加开发难度的情况下做到能满足需求
  
   - 以 CGI 模式安装时
   
     - 可能受到的攻击(http://php.net/manual/zh/security.cgi-bin.attacks.php)
     - 安全的 chroot 和 setuid 环境
     
   - [以 Apache 模块安装时](http://php.net/manual/zh/security.apache.php)
   
   - [会话（Session）安全](http://php.net/manual/zh/book.session.php)
     - 基本用法
     
       - 通过为每个独立用户分配唯一的会话 ID，可以实现针对不同用户分别存储数据的功能。 会话通常被用来在多个页面请求之间保存及共享信息。 一般来说，会话 ID 通过 cookie 的方式发送到浏览器，并且在服务器端也是通过会话 ID 来取回会话中的数据。 如果请求中不包含会话 ID 信息，那么 PHP 就会创建一个新的会话，并为新创建的会话分配新的 ID。
     
         会话的工作流程很简单。当开始一个会话时，PHP 会尝试从请求中查找会话 ID （通常通过会话 cookie）， 如果请求中不包含会话 ID 信息，PHP 就会创建一个新的会话。 会话开始之后，PHP 就会将会话中的数据设置到 $_SESSION 变量中。 当 PHP 停止的时候，它会自动读取 $_SESSION 中的内容，并将其进行序列化， 然后发送给会话保存管理器来进行保存。
       
         默认情况下，PHP 使用内置的文件会话保存管理器（files）来完成会话的保存。 也可以通过配置项 session.save_handler 来修改所要采用的会话保存管理器。 对于文件会话保存管理器，会将会话数据保存到配置项 session.save_path 所指定的位置。
       
         可以通过调用函数 session_start() 来手动开始一个会话。 如果配置项 session.auto_start 设置为1， 那么请求开始的时候，会话会自动开始。
       
         PHP 脚本执行完毕之后，会话会自动关闭。 同时，也可以通过调用函数 session_write_close() 来手动关闭会话。
     - 保持 HTTP 会话管理的安全是重要的。会话安全相关内容描述章节在[Session 模块](http://php.net/manual/zh/book.session.php) 文档下的[会话安全](http://php.net/manual/zh/session.security.php)部分。
     - [传送会话ID](http://php.net/manual/zh/session.idpassing.php)
       
       - 有两种方式用来传送会话 ID
       
         - Cookies
         - URL 参数

