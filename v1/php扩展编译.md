### 编译安装php扩展
  
  - 有时默认没有安装一些扩展， 但又不想重新编译安装php, 可以单独安装扩展
  - 废话不多说，举个例子, php7默认不安装fileinfo扩展, 但是很多应用用到它

```shell
# 进入源码包的扩展库目录,注意是源码包，而不是编译后的php安装目录
cd /usr/local/src/php-7.0.23/ext/fileinfo/  

# 找到php安装目录的bin, 确定好phpize的路径, 方便下面操作

# 不离开php安装源码的ext/fileinfo目录，执行以下命令
/usr/local/php/bin/phpize

返回
Configuring for:
PHP Api Version:         20151012
Zend Module Api No:      20151012
Zend Extension Api No:   320151012
则执行下一步
./configure --with-php-config=/usr/local/php/bin/php-config
make && make install

返回以下命令行说明安装成功了~
Build complete.
Don't forget to run 'make test'.
Installing shared extensions:     /usr/local/php/lib/php/extensions/no-debug-non-zts-20060613/

# 然后修改php.ini配置,加入扩展启用
extension=fileinfo.so

# 最后重启php
service php-fpm restart
```