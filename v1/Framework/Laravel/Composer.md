### composer的安装和使用

- windows下安装请参考资料

  - http://blog.csdn.net/crazywoniu/article/details/73432291
  - http://blog.csdn.net/iloveyougirls/article/details/52333597
  - openssl开启http://www.ituring.com.cn/article/261281

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
   
### 关于下载源码后如何运行

example:

   ```git clone git@github.com:GouKouRuri/cms.git```
  

- 下载源码后安装相关依赖包和库
 
   ```composer install```
   
- 更新包(composer.json修改后执行)

   ```composer update```
   
- 添加包
   `composer require "foo/bar:1.0.0"`
   
- laravel下配置.env和生成key

   ```cp .env.example .env```
   
   ```php artisan key:generate```
   
- 在config/database.php配置数据库
- 迁移建表

  ```php artisan migrate```
  
  
- composer dump 按照配置环境重新加载

- Laravel项目的app文件夹下的所有目录都使用 PSR-4自动加载标准被自动加载，所以你可以在其中随心所欲地创建需要的目录
  ```
   "psr-4": {
     "App\\": "app/"  
   },
   ```
   App是app/的映射名称可以改成自己想要的


  