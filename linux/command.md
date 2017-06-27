## linux的常用命令

* 目录处理命令
  - ls

    -a 显示所有文件,包括隐藏文件

    -l 显示详细信息（ls -lh 显示的文件大小可以人性化显示）

    -d 查看目录属性

    -i 显示文件节点(每个文件都有一个节点，但一个节点可以对应多个文件，硬链接的文件与源文件有相同的节点)

  - mkdir

    -p 递归创建目录

  - pwd 显示当前目录

  - cd 切换目录

  - cp

    -r 可以复制目录

    -p 保留文件属性(备份日志时不希望文件更新时间发生改变)

  - mv 移动文件

  - rm

    -r 可以删除目录

    -f 强制执行

* 文件处理命令

  - touch 创建一个空文件(如果创建带空格名文件时用双引号引起来)

  - cat
    -n 显示文件内容(带行号)

  - tac 倒着显示文件内容

  - more 分页显示文件内容

     空格或者f 翻页
     enter 换行
     q 退出

  -  less 和more一样,但是可以上翻页

     / 搜索内容 n 继续查找

  - head -n 查看文件前几行

  - tail

    -n (指定行数) 查看文件末尾几行

    -f 动态显示文件末尾内容(比如看动态日志)

* 链接命令

  - ln -s [源文件] [目标文件] 生成软链接

  - ln [源文件] [目标文件]    

  硬链接: 同步更新，一个丢失对另一个不影响

  软链接: 相当于快捷方式,指向源文件, 权限是lrwxrwxrwx

* 权限管理命令(文件权限更改只能是文件所有者或者root)

  - chmod

    chmod [ugoa][+-=][rwx] 文件名或者目录   -- 多个设置用逗号隔开,example: chmod u+rx,g-x,o+rw,a+r aaa.php

    chmod -R 777 文件名或者目录 递归修改权限



    rwx权限在文件和目录的区别

    文件--r: 查看文件内容,w:修改文件内容,x:执行文件
    目录--r: 列出目录的内容，查看和复制目录文件,w:在目录中创建和删除文件,x进入目录的权限

  - chown [用户名] [文件名或者目录] 改变文件或者目录的所有者

  - chgrp [用户组] [文件名或者目录] 改变文件或者目录的所属组

  - umask -S 修改默认新建时分配的权限(文件比较特殊默认新建都没有x权限)

* 文件搜素命令
  
  - find  文件搜索
    
    find [搜索范围] [匹配条件]
    
    - example:
      
      * 匹配0个以上字符
      ? 匹配单个字符
      $ 结束
      ```
      -name 根据文件名查找
      -iname 根据文件名查找，不区分大小写
      -size  根据文件大小查找
      -user  根据所有者查找
      -group 根据所属组查找
      -amin  根据访问时间改变查找
      -cmin  根据文件属性改变查找
      -mmin  根据文件内容改变查找
      -a 两个条件同时满足
      -o 两个条件满足其中一个
      -type 根据文件类型查找(f文件 d目录 l软链接文件)
      -inum 根据i节点查找
      -exec/-ok [命令] {} \; 对查找的结果进行操作(-ok会询问)
      ```
      
      ```find /etc -name *init*```
      
      ```find /etc -name *init???```
      
      ```find /etc -size +204800```  /etc目录搜索大于100M的文件
      
      linux里1个数据块是512字节，0.5k,+大于,-小于，不写是等于
      
      ```find /home -user /develop```
      
      ```find /home -cmin -5```  查找5分钟内被修改过属性的文件
      
      +大于, -小于
      
      ```find /etc -size +163840 -a -204800``` 查找/etc目录里大于80M并且小于100M的文件
      
      ```find /etc -iname init* -a -type d```  
      
      ```find /etc -iname intt* -a type f -exec ls -l {} \;
      
* 其他文件搜索命令
  
  - locate 在资料库中查找(资料库会自动定期更新，但是新建的文件短时间内不会被收录无法搜索)
  
    - locate [文件名]
    - locate locate 可以查看资料库
    - updatedb 手动更新资料库(tmp等文件下是不是被收录)
    - locate -i [文件名]   不区分大小写查找文件
    
  - which 搜索命令所在的目录及别名信息
  
    example: which ls
    
    别名：例如cp,rm等都是有别名,rm=rm -i 本身不询问,别名是询问

  - whereis 搜索命令所在的目录以及帮助文档所在的路径
  
  - grep 在文件内容内查找关键词对应的行
  
    ```grep -i muliuser /etc/inittab``` 不区分大小写查找
    
    ```grep -v ^# /etc/inittab``` 去掉行首以#开头的行,去注释非常方便
    
* 帮助命令
  
  - man 原意manual, 1是命令帮助，5是配置文件的帮助，优先显示命令的帮助
  
    查看配置文件或者命令的帮助信息,跟more文本操作一样
    
    ```man ls```
    
    ```man services```
    
    ```man 5 passwd```  查看passwd配置文件的帮助
    
* 用户管理命令

  - useradd [用户名] 添加用户名
  - passwd [用户名]  为用户设置密码
  - who   查看登录用户的信息
    
    - 登录用户名  登录终端(tty:本地终端,pts远程终端) 登录时间  登录的主机的ip地址,没写就是本机登录
  
  - w  查看登录用户的详细信息(含有负载信息,idle:用户登录后的空闲时间,pcpu用户登录后执行操作占用cpu的时间,)
  
    - uptime 查看linux服务器运行时间
    
* 压缩解压命令

  - 常见的压缩格式：.gz,.zip,.rar
  
    - gzip [文件名] 压缩成.gz格式   --- gzip只能压缩文件,不能压缩目录，并且压缩完源文件就没有了
    - gunzip [文件名] 解压缩.gz文件
    
    - tar [压缩后的文件名] [需要压缩的文件或者目录]
    
      -c 打包(把多个文件或者目录打包成一个文件)
      
      -v 显示详细信息
      
      -f 指定文件名
      
      -z 打包同时压缩
      
      -x 解包
      
      example:
      
      ```tar -zcf etc.tar.gz /etc```  把etc目录打包压缩成etc.tar.gz
      
      ```tar -zxf etc.tar.gz```   把etc.tar.gz解压缩
      
    - zip(在windows和linux下均支持)
    
      - zip [压缩后的文件名] [需要压缩的文件]
      - zip -r [压缩后的文件名] [需要压缩的文件或者目录]
      
    - unzip
    
      - unzip [解压缩的文件]
      
* 网络命令

  - write [用户名]  给在线用户发送信息,ctrl+D文本输入结束
  
  - wall [message] 给所有用户发送信息
  
  - ping  [ip地址]  测试网络是否可以连通
  
    -c [次数] 指定发送次数
    
  - ifconfig 查看当前的网络状态
  
    eth0 表示本地的真实网卡
    
    lo 回环地址，127.0.0.1永远都能连通,没网没卡都可以
    
    网络类型：以太网    mac地址/网卡的硬件地址
  
    计算机当前的ip地址   当前网络的广播地址
    
    设置网卡ip地址： ifconfig eth0 192.168.8.250
    
  - mail [用户名] 查看发送邮件
  
  - last 统计计算机所以用户的登陆信息和计算机的重启信息
  
  - lastlog
  
    lastlog -u [uid] 查看用户登录信息
    
  - traceroute 显示数据包到主机间的路径 ---这个命令ubuntu有时需要下载安装包才可以
  
  - netstat [选项] 显示网络相关信息
  
    ```
    -t  TCP协议(传输协议之一,三次握手建立连接,面向连接,及时稳定,比如http)
    -u  UDP协议(更快，但是不安全稳定)
    -l  监听
    -r  路由
    -n  显示ip地址和端口号
    ```
    
    example：
    ```
    netstat -tlun  查看本机监听的端口
    netstat -an    查看本机所有的网络连接
    netstat -rn    查看本机路由表,网关
    ```
  
  - setup       ---redhat系特有的设置网络的工具
    
  - mount   挂载命令
    
    ```
    mount -t iso9600 /dev/sr0  /mnt/cdrom/
           文件系统   设备文件名  挂载点
    ```
  
  -umount 卸载命令
  
   ```
    umount /dev/sr0
   ```
   
* 关机重启命令 ----真实服务器应该关闭所有服务,尽量使用shutdown重启,其他的不推荐

  - shutdown [选项] [时间]
    
    -c 取消前一个关机命令
    
    -h 关机
    
    -r 重启
    
  - halt 关机
  - poweroff 关机
  - init 0 关机
  - reboot 重启
  - init 6 重启
  
  ```
  init 七个系统运行级别
  0 关机 1单用户 2不完全多用户,不含NFS服务(网络文件系统,实现两个linux系统之间文件共享) 3完全多用户 4未分配 5图形界面 6重启 
  cat /etc/inittab 修改系统的默认运行级别
  runlevel 查看系统运行级别
  ```
  
  - logout 退出登录    --- 不用时必须要使用
    
  
    
     
      
     
    
      
      
          
      
