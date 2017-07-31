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
   
   - 会话（Session）安全
   
     - 保持 HTTP 会话管理的安全是重要的。会话安全相关内容描述章节在[Session 模块](http://php.net/manual/zh/book.session.php) 文档下的[会话安全](http://php.net/manual/zh/session.security.php)部分。

