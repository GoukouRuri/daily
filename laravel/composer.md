### composer的安装和使用

- 查看php版本是否符合

  输入命令```php-v```查看php版本
  
  php5.4及以上才能符合
  
- 安装setup

  ```php -r "copy('https://install.phpcomposer.com/installer', 'composer-setup.php');"```
  
  ```php composer-setup.php```
  
  ```php -r "unlink('composer-setup.php');"```
  
  上述 3 条命令的作用依次是：
  
  - 下载安装脚本 － composer-setup.php － 到当前目录。
  - 执行安装过程。
  - 删除安装脚本。
  
- 全局安装---(如果想要局部安装,网上有)

  ```sudo mv composer.phar /usr/local/bin/composer```
  
- 更换镜像源----重点：如果没有翻墙请一定要用这步更换到国内镜像，默认是国外镜像
  
    ```composer config -g repo.packagist composer https://packagist.phpcomposer.com```
    
- 具体使用及相关配置请查看官网

   http://docs.phpcomposer.com/
  