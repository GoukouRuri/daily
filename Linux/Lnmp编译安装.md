> ### 安装nginx

- 安装相关依赖

  - `yum install gcc-c++`                         //安装gcc
  - `yum install -y pcre pcre-devel`              
  - `yum install -y zlib zlib-devel`
  - `yum install -y openssl openssl-devel`


- 下载nginx源代码

  - `cd /usr/local/src`
  - `wget http://nginx.org/download/nginx-1.10.3.tar.gz`
  - `tar -zxvf nginx-1.10.3.tar.gz`

- 编译nginx

  `cd nginx-1.10.3`
  ```
  ./configure \
  --prefix=/usr/local \
  --sbin-path=/usr/sbin/nginx \
  --conf-path=/etc/nginx/nginx.conf \
  --error-log-path=/var/log/nginx/error.log \
  --http-log-path=/var/log/nginx/access.log \
  --pid-path=/var/run/nginx/nginx.pid  \
  --lock-path=/var/lock/nginx.lock \
  --user=nginx \
  --group=www \
  --with-http_ssl_module \
  --with-http_flv_module \
  --with-http_stub_status_module \
  --with-http_gzip_static_module \
  --http-proxy-temp-path=/var/tmp/nginx/proxy/ \
  --http-fastcgi-temp-path=/var/tmp/nginx/fcgi/ \
  --http-uwsgi-temp-path=/var/tmp/nginx/uwsgi \
  --http-scgi-temp-path=/var/tmp/nginx/scgi \
  --with-pcre
  ```

  - `make && make install`

- 创建启动脚本,在/etc/init.d/nginx写入shell脚本

```sh
#!/bin/sh
# nginx - this script starts and stops the nginx daemon
#

# chkconfig:   - 85 15 
# description:  Nginx is an HTTP(S) server, HTTP(S) reverse \
#               proxy and IMAP/POP3 proxy server
# processname: nginx
# config:      /etc/nginx/nginx.conf
# config:      /etc/sysconfig/nginx
# pidfile:     /var/run/nginx.pid

# Source function library.
. /etc/rc.d/init.d/functions

# Source networking configuration.
. /etc/sysconfig/network

# Check that networking is up.
[ "$NETWORKING" = "no" ] && exit 0

nginx="/usr/sbin/nginx"
prog=$(basename $nginx)

NGINX_CONF_FILE="/etc/nginx/nginx.conf"

[ -f /etc/sysconfig/nginx ] && . /etc/sysconfig/nginx

lockfile=/var/lock/subsys/nginx

make_dirs() {
   # make required directories
   user=`nginx -V 2>&1 | grep "configure arguments:" | sed 's/[^*]*--user=\([^ ]*\).*/\1/g' -`
   options=`$nginx -V 2>&1 | grep 'configure arguments:'`
   for opt in $options; do
       if [ `echo $opt | grep '.*-temp-path'` ]; then
           value=`echo $opt | cut -d "=" -f 2`
           if [ ! -d "$value" ]; then
               # echo "creating" $value
               mkdir -p $value && chown -R $user $value
           fi
       fi
   done
}

start() {
    [ -x $nginx ] || exit 5
    [ -f $NGINX_CONF_FILE ] || exit 6
    make_dirs
    echo -n $"Starting $prog: "
    daemon $nginx -c $NGINX_CONF_FILE
    retval=$?
    echo
    [ $retval -eq 0 ] && touch $lockfile
    return $retval
}

stop() {
    echo -n $"Stopping $prog: "
    killproc $prog -QUIT
    retval=$?
    echo
    [ $retval -eq 0 ] && rm -f $lockfile
    return $retval
}

restart() {
    configtest || return $?
    stop
    sleep 1
    start
}

reload() {
    configtest || return $?
    echo -n $"Reloading $prog: "
    killproc $nginx -HUP
    RETVAL=$?
    echo
}

force_reload() {
    restart
}

configtest() {
  $nginx -t -c $NGINX_CONF_FILE
}

rh_status() {
    status $prog
}

rh_status_q() {
    rh_status >/dev/null 2>&1
}

case "$1" in
    start)
        rh_status_q && exit 0
        $1
        ;;
    stop)
        rh_status_q || exit 0
        $1
        ;;
    restart|configtest)
        $1
        ;;
    reload)
        rh_status_q || exit 7
        $1
        ;;
    force-reload)
        force_reload
        ;;
    status)
        rh_status
        ;;
    condrestart|try-restart)
        rh_status_q || exit 0
            ;;
    *)
        echo $"Usage: $0 {start|stop|status|restart|condrestart|try-restart|reload|force-reload|configtest}"
        exit 2
esac
```    
 
- 更改脚本权限为755

  `chmod 755 /etc/init.d/nginx`


- 配置nginx用户和用户组

  - `groupadd -r www`
  - `useradd -r -g nginx -s /bin/false -M www`        
  - `id nginx`

- 讲脚本添加到service服务中

  - `chkconfig --add nginx`
  - `service nginx reload`
  - `chkconfig nginx on`

- 启动nginx

  - `service nginx start`

- 查看nginx状态

  - `ps -aux | grep nginx`

***

> ### 安装Mysql

- 安装相关依赖

  - `yum -y install cmake`
  - `yum -y install bison-devel`
  - `yum -y install ncurses-devel`
  
- 下载mysql源代码

  - `wget http://cdn.mysql.com//Downloads/MySQL-5.6/mysql-5.6.28.tar.gz` //如果下载地址失效，请前往mysql.com官网自行下载
  - `tar -xzvf mysql-5.6.28.tar.gz` 
  - `cd mysql-5.6.28`
  
- 编译安装

  - 配置选项
```
cmake \
-DCMAKE_INSTALL_PREFIX=/usr/local/mysql \
-DMYSQL_DATADIR=/usr/local/mysql/data \
-DSYSCONFDIR=/etc \
-DWITH_MYISAM_STORAGE_ENGINE=1 \
-DWITH_INNOBASE_STORAGE_ENGINE=1 \
-DWITH_MEMORY_STORAGE_ENGINE=1 \
-DWITH_READLINE=1 \
-DMYSQL_UNIX_ADDR=/var/lib/mysql/mysql.sock \
-DMYSQL_TCP_PORT=3306 \
-DENABLED_LOCAL_INFILE=1 \
-DEXTRA_CHARSETS=all \
-DDEFAULT_CHARSET=utf8 \
-DDEFAULT_COLLATION=utf8_general_ci
```
   如果出现以下警告则去掉上面配置中的两项
```
CMake Warning:
Manually-specified variables were not used by the project:

WITH_MEMORY_STORAGE_ENGINE

WITH_READLINE
```

  去掉的两项
  `-DWITH_MEMORY_STORAGE_ENGINE=1 \`
  `-DWITH_READLINE=1 \`
  
  - 编译和安装
  
  `make`      //此处编译比较久
  `make install`
  
- 配置mysql用户和用户组

  `groupadd mysql`
  `useradd -g mysql mysql`
  
- 修改/usr/local/mysql权限

  `chown -R mysql:mysql /usr/local/mysql`
  
- 安装perl扩展,否则mysql初始化时会报出这样的错误`./scripts/mysql_install_db: /usr/bin/perl: bad interpreter: No such file or directory`
  
  `yum -y install perl perl-devel`

- 进入安装路径执行mysql初始化脚本,创建系统自带的数据库和表

  `scripts/mysql_install_db --basedir=/usr/local/mysql --datadir=/usr/local/mysql/data --user=mysql`
     
- 将 MySQL 提供的sysv风格的服务脚本复制到 /etc/init.d/mysql目录

  `cp support-files/mysql.server /etc/init.d/mysql`
  
- 设置开启启动

  `chkconfig mysql on`
  
- 启动mysql

  `/etc/init.d/mysql start`
  
  此处如果报以下错误`MySQL: Starting MySQL….. ERROR! The server quit without updating PID file`
  
  请参考http://www.cnblogs.com/minbbp/p/3884804.html
  
  - 使用`mv /etc/my.cnf /etc/my.cnf.backup`后在执行`/etc/init.d/mysql start`重启mysql
  
- 将 MySQL 加入环境变量，修改/etc/profile文件，在文件末尾添加

  ```
  PATH=/usr/local/mysql/bin:$PATH
  export PATH
  ```
  
- 保存并关闭文件，运行下面的命令让配置生效

  `source /etc/profile`
  
- 最后配置mysql root用户的密码

  `mysql -uroot` 进入mysql命令行界面
  `set password = password('你要设定的密码')`

- 至于优化mysql配置和防火墙配置可以自行google

***

> ### 安装php

  - 备注(php必须放在三个的最后一个进行安装,因为需要对mysql和nginx进行配置,lamp环境也是一样的)
  
- 安装前准备安装相关的依赖

  - `yum install -y libxm12 libjpeg libjpeg-devel libpng libpng-devel freetype freetype-devel libxml2 libxml2-devel glibc glibc-devel glib2 glib2-devel bzip2 bzip2-devel ncurses ncurses-devel curl curl-devel e2fsprogs e2fsprogs-devel krb5 krb5-devel openssl openssl-devel openldap openldap-devel nss_ldap openldap-clients openldap-servers php-mysqlnd libmcrypt-devel libtidy libtidy-devel recode recode-devel libxpm-devel`
  
- 下载php7源代码

  - ```
     wget http://cn2.php.net/distributions/php-7.0.2.tar.gz
     tar -xzvf php-7.0.2.tar.gz
     cd php-7.0.2
     ```
- 编译安装

  - 配置（这里的配置已经优化过的,如果是网上随便抄来的有很多问题,例如--with-mysql选项和--enable-fastcgi早已去除,如果加了反而报错）
  
  `./configure --prefix=/usr/local/php7 --with-config-file-path=/etc/php7 --with-pdo-mysql=mysqlnd --with-mysqli=mysqlnd --with-gd --with-iconv --with-zlib --enable-xml --enable-bcmath --enable-shmop --enable-sysvsem --enable-inline-optimization --enable-mbregex --enable-fpm --enable-mbstring --enable-ftp --enable-gd-native-ttf --with-openssl --enable-pcntl --enable-sockets --with-xmlrpc --enable-zip --enable-soap --without-pear --with-gettext --enable-session --with-mcrypt --with-curl --with-jpeg-dir --with-freetype-dir --with-xpm-dir=/usr --with-bz2`
  
   配置时仍会出现报错，一般是相关依赖的devel开发包没有安装,有时需要开发包里的头文件,例如下面参考解决报错问题,报错可能很多需要耐心解决
   
   这里列出 PHP 编译配置常见错误和解决办法:
   
    ```
    configure: error: xslt-config not found. Please reinstall the libxslt >= 1.1.0 distribution
    
    yum install libxslt-devel
    configure: error: Could not find net-snmp-config binary. Please check your net-snmp installation.
    
    yum install net-snmp-devel
    configure: error: Please reinstall readline - I cannot find readline.h
    
    yum install readline-devel
    configure: error: Cannot find pspell
    
    yum install aspell-devel
    checking for unixODBC support... configure: error: ODBC header file '/usr/include/sqlext.h' not found!
    
    yum install unixODBC-devel
    configure: error: Unable to detect ICU prefix or /usr/bin/icu-config failed. Please verify ICU install prefix and make sure icu-config works.
    
    yum install libicu-devel
    configure: error: utf8mime2text() has new signature, but U8TCANONICAL is missing. This should not happen. Check config.log for additional information.
    
    yum install libc-client-devel
    configure: error: freetype.h not found.
    
    yum install freetype-devel
    configure: error: xpm.h not found.
    
    yum install libXpm-devel
    configure: error: png.h not found.
    
    yum install libpng-devel
    configure: error: vpx_codec.h not found.
    
    yum install libvpx-devel
    configure: error: Cannot find enchant
    
    yum install enchant-devel
    configure: error: Please reinstall the libcurl distribution - easy.h should be in /include/curl/
    ```
    
  - 编译安装
  
    `make && make install`
    
    如果这里出现报错`libtool: link: ext/reflection/php_reflection.lo is not a valid libtool object make:*libtool: link: ext/libxml/libxml.lo' is not a valid libtool object` 请清掉编译缓存文件重新编译,如下
    
    `make clean`
至此nginx,mysql,php已全部安装就位,但是nginx本身不能处理PHP，它只是个web服务器，当接收到请求后，如果是php请求，则发给php解释器处理，并把结果返回给客户端。所有接下来配置nginx服务器    
***

> ### 配置nginx服务器

- nginx一般是把请求发fastcgi管理进程处理，fascgi管理进程选择cgi子进程处理结果并返回被nginx

  首先修改 Nginx 的配置，刚才安装时配置的配置文件目录是 /etc/nginx/nginx.conf
  
  `vim /etc/nginx/nginx.conf`
  
  修改server里location部分
    - 原配置
    ```
    server {
        listen 80;
        server_name _;
        access_log /data/wwwlogs/access_nginx.log combined;
        root /data/wwwroot/default;
        index index.html index.htm index.php;
        #error_page 404 /404.html;
        #error_page 502 /502.html;
        location /nginx_status {
          stub_status on;
          access_log off;
          allow 127.0.0.1;
          deny all;
        }
        location ~ [^/]\.php(/|$) {
          #fastcgi_pass remote_php_ip:9000;
          fastcgi_pass unix:/dev/shm/php-cgi.sock;
          fastcgi_index index.php;
          include fastcgi.conf;
        }
        location ~ .*\.(gif|jpg|jpeg|png|bmp|swf|flv|mp4|ico)$ {
          expires 30d;
          access_log off;
        }
        location ~ .*\.(js|css)?$ {
          expires 7d;
          access_log off;
        }
        location ~ /\.ht {
          deny all;
        }
    }


    ```
  ```
    user www www    //nginx以www用户身份和www用户组运行
    location / {
         root   /var/www;
         index   index.html  index.htm  index.php;
     }

    location ~ .php$ {
        root /var/www; //web服务根目录 
        fastcgi_pass 127.0.0.1:9000;
        fastcgi_index index.php;
        fastcgi_param SCRIPT_FILENAME /var/www$fastcgi_script_name;
        include fastcgi_params;
    }
  ```
  修改php-fpm.d/www.conf
  ```
  user www
  group www
  ``` 
- 初始化配置文件

  - `cp /usr/local/php7/etc/php-fpm.conf.default  /usr/local/php7/etc/php-fpm.conf`
  - `cp /usr/local/php7/etc/php-fpm.d/www.conf.default  /usr/local/php7/etc/php-fpm.d/www.conf`
  
- 启动php-fpm

  `/usr/local/php7/sbin/php-fpm`
  
- 测试一下在web服务服务目录写入php代码

  ```
  cd /var/www
  touch index.php
  chmod a+x index.php
  echo '<?php echo phpinfo();' > index.php
  `

- 补充添加mysql和php环境变量,写入配置文件中永久生效,在/etc/profile文件的末尾加入两行代码

`PATH=$PATH:/usr/local/php7/bin:/usr/local/mysql/bin`             // 具体是自己安装的路径
`export PATH`

保存退出后执行source /etc/profile是配置生效
echo $PATH 查看当前环境变量是否已经生效

***

- 如何在远程vps搭建的环境允许外网访问数据库（方便个人使用,生产环境的不建议开发给外部入口）

  - 设置防火墙,允许mysql的3306端口,修改/etc/sysconfig/iptables,添加下面的一行代码
  
    `-A INPUT -m state --state NEW -m tcp -p tcp --dport 3306 -j ACCEPT`
    
     执行service iptables restart 重启防火墙
     
  - 配置远程连接授权 （一般不会出现到这部，除非是自己建的用户，否则root权限很大）
  
    ```
    mysql -uroot -p
    use mysql;
    grant all privileges  on *.* to root@'%' identified by "root";
    update user set host = '%' where user = 'root';
    ```
    可能会出现`ERROR 1062 (23000): Duplicate entry '%-root' for key 'PRIMARY' `保错,不用管
    执行flush privileges;此时远程连接可以使用了

*** 

至此完成lnmp编译安装,相关依赖不用编译安装，是因为不需要也没必要，即便编译也是使用默认配置,而且编译安装依赖十分繁多

-- The End     Writed By GoukouRuri
***
   