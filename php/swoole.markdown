### laravel-swoole使用方法

- centos环境下为php安装指定版本的swoole扩展
  
  - 安装pcel
    ```shell
    sudo yum install php-dev php-pear autoconf automake libtool  -y 
    ```

  - [安装包页面](https://pecl.php.net/package/swoole)找到需要的版本安装swoole
    ```shell
    pecl install https://pecl.php.net/get/swoole-1.9.23.tgz
    ```

  - 修改php.ini配置并重启fpm
  
    - 在php.ini中加入`extension=swoole.so`
    - 重启fpm
    - `php -m |grep swoole` 查询是否安装好swoole