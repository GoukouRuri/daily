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
  

