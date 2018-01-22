> ### Apache配置虚拟域名

  ###### 假如我们有多个项目的时候, 我们需要定制本地的虚拟域名

* 定制虚拟域名涉及两处:

  - 1、虚拟域名配置文件httpd-vhosts.conf
    
    - 配置如下
    ```apacheconfig
    ###开始
    NameVirtualHost *:80
    <VirtualHost *:80>
    ServerName localhost
    DocumentRoot "D:/WWW/WEB"
    AllowEncodedSlashes On
    <Directory "D:/WWW/WEB">
    Options FollowSymLinks IncludesNOEXEC Indexes
    DirectoryIndex index.php index.html
    AllowOverride All
    Order Deny,Allow
    Allow from all
    Require all granted
    RewriteCond %{REQUEST_METHOD} ^(TRACE|TRACK)
    RewriteRule .* - [F]
    </Directory>
    </VirtualHost>
     
    <VirtualHost *:80>
    ServerName www.test.com
    ServerAlias test.com
    DocumentRoot "D:/WWW/WEB/test"
    AllowEncodedSlashes On
    <Directory "D:/WWW/WEB/test">
    Options FollowSymLinks IncludesNOEXEC Indexes
    DirectoryIndex index.php index.html
    AllowOverride All
    Order Deny,Allow
    Allow from all
    Require all granted
    RewriteCond %{REQUEST_METHOD} ^(TRACE|TRACK)
    RewriteRule .* - [F]
    </Directory>
    </VirtualHost>
    ###结束
    ```
 
  - 2、hosts文件
  
    - 配置如下
    ```
    127.0.0.1 localhost
     
    127.0.0.1 www.test.com
     
    127.0.0.1 test.com

    ```
    
> ### Windows系统下如何配置多个apache服务器

  - 参考资料http://blog.csdn.net/demon3182/article/details/51554261
  - 非80端口需要加地址栏端口号比较麻烦,另外的apache服务需要手动运行,不是很方便
  
> ### Windows系统下如何一个apache服务器运行多个php版本

  - 需要使用fcgid模块配置多个PHP版本共存(一般phpstudy环境都已经有了,没有需要根据apache版本下载对应的 mod_fcgid-2.3.9-win64-VC14.zip) https://www.apachelounge.com/download/
  - 配置默认php版本, httpd.conf默认配置改成
```apacheconfig
LoadModule fcgid_module modules/mod_fcgid.so #使用fcgid模块
AddHandler fcgid-script .fcgi .php
FcgidInitialEnv PHP_FCGI_MAX_REQUESTS 1000
FcgidMaxRequestsPerProcess 1000
FcgidMaxProcesses 15
FcgidIOTimeout  120
FcgidIdleTimeout  120
AddType application/x-httpd-php .php
# 全局默认使用的PHP版本配置
FcgidInitialEnv PHPRC "C:/ProgramFiles(x86)/php5.6"
FcgidWrapper "C:/ProgramFiles(x86)/php5.6/php-cgi.exe" .php
# 上传文件的最大尺寸 100MB
FcgidMaxRequestLen 104857600  # 当你上传文件的时候发现总是出现500错误，而程序其实没有错误。 实际上是因为上传内容体积过大，即便修改了php.ini 中配置的上传参数也没有用的，必须修改这里才行，nginx下也会有类似的问题
```
  - 对需要不同 PHP 版本的设置 httpd-vhosts.conf 添加下面代码,加在VirtualHost里,但不在Directory里
```apacheconfig
# 这里的路径必须写成正斜杠,windows系统下写反斜杠也会导致apache无法启动,原因未知!
FcgidInitialEnv PHPRC "C:/ProgramFiles(x86)/php7.0/"   
FcgidWrapper "C:/ProgramFiles(x86)/php7.0/php-cgi.exe" .php
```
  - 重启apache
  - .htaccess 的重定向配置
  
    以前是这样用的`RewriteRule ^(.*)$ index.php/$1 [QSA,PT,L]`,会无法重定向到index.php,出现No input file specified.报错.改成`RewriteRule ^(.*)$ index.php [L,E=PATH_INFO:$1]`即可
    
  

