> ### HTTP协议与SPDY协议
  
  - http协议详解
  - http协议如何工作
  - http协议的应用
  - 垃圾信息如何防御
  
    - IP限制
    - 验证码
    - Token和表单欺骗
    - 审核机制
    
  - 如何抓包及进行http断点测试
  
> ### [Socket](https://baike.baidu.com/item/socket/281150?fr=aladdin)进程通信机制和应用（网络开发必会内容）

    `网络上的两个程序通过一个双向的通信连接实现数据的交换，这个连接的一端称为一个socket。
    建立网络通信连接至少要一对端口号(socket)。socket本质是编程接口(API)，对TCP/IP的封装，TCP/IP也要提供可供程序员做网络开发所用的接口，这就是Socket编程接口；HTTP是轿车，提供了封装或者显示数据的具体形式；Socket是发动机，提供了网络通信的能力。
    Socket的英文原义是“孔”或“插座”。作为BSD UNIX的进程通信机制，取后一种意思。通常也称作"套接字"，用于描述IP地址和端口，是一个通信链的句柄，可以用来实现不同虚拟机或不同计算机之间的通信。在Internet上的主机一般运行了多个服务软件，同时提供几种服务。每种服务都打开一个Socket，并绑定到一个端口上，不同的端口对应于不同的服务。Socket正如其英文原意那样，像一个多孔插座。一台主机犹如布满各种插座的房间，每个插座有一个编号，有的插座提供220伏交流电， 有的提供110伏交流电，有的则提供有线电视节目。 客户软件将插头插到不同编号的插座，就可以得到不同的服务。
    `
  
  - 进程通信的相关概念
    
    - 端口
    - 地址
    - 连接
  - Socket实现服务器端和客户端之间的交互
  - Socket函数原型
  - Socket交互应用：使用Socket抓取数据
  - CURL工具和应用
  
    - 建立curl请求
    - 检查curl错误与返回信息
    - 在curl中伪造头信息
    - 在curl中用post方法发送数据
    - 使用curl上传文件
    - curl批处理
    - curl设置项

> ### 邮件传输协议SMTP

  - smtp协议如何工作
  - smpt协议常用命令
  - smpt协议应用：如何发送邮件

> ### WebService(web开发重点)

  - 概念
  - 认识PHPRPC协议
  - web服务的实现模式
  - 简单的对象访问协议SOAP

> ### Cookie与Session(web开发重点)

  - cookie的基本概念和设置
  - php和javascript对cookie的操作及不同
  - cookie的存储机制和应用
  - cookie的跨越与p3p协议
  - 本地存储localStorage
  - session的基本概念和设置
  - session的工作原理
  - session的入库
  - cookie与session区别与错误理解纠正

