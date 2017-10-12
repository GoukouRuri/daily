## laravel 快速食用指南
  
  - ```author: GoukouRuri```
  - ```time: 2017-06-24 20:15```

###### laravel 目录结构（仅适用于version5.1,5.2，写作时的最新版本5.3目录结构有很大区别）

- app 包含Controller,Models,路由等在内的应用目录,大部分业务在这个目录下

  - console 命令行程序目录
  
    - 包含了用于命令行执行的类,可以在这个目录自定义类
    - kernel.php  命令调用内核文件,包含commands变量(命令清单，自定义的命令需要加入到这里)和schedule方法(用于任务调度，即定时任务)
  - Events 事件目录
  
  - Exceptions  包含了自定义的错误和异常处理类
  
  - Http   http传输层相关的类目录
    
    - Controllers 控制器目录
    - Middleware  中间件目录
    - Requests    请求类目录
    - kernel.php  包含http中间件和路由中间件的内核文件
    - routes.php  强大的路由
  
  - Jobs 该目录下包含队列的任务类
  - Listeners 监听器目录
  - Providers 服务提供者目录
  - User.php  自带的模型实例,我们新建的目录默认在该目录,可以自定义到一个Models目录
  
- bootstrap   框架启动载入目录
  
  - app.php 创建框架的应用实例
  - autoload.php  自动加载
  - cache 存放框架启动缓存,web服务器需要有该目录的写入权限

- config 各种配置文件的目录

  - app.php  系统级配置文件
  - auth.php 用户身份认证配置文件,指定好table和model就可以很方便的使用身份认证功能
  - broadcasting.php 事件广播配置文件
  - cache.php 缓存配置文件
  - compile.php 编译额外的类和文件需要的配置文件,很少用到
  - database.php 数据库配置文件
  - filesystems.php 文件系统配置文件,这里可以配置云存储参数
  - mail.php 电子邮件配置文件
  - queue.php 消息队列配置文件
  - services.php 可存放第三方服务的配置文件
  - session.php 配置session的存储方式，生命周期等信息
  - view.php 模版文件配置文件,包含模版目录和编译目录等

- database  数据库相关目录
  
  - factories  5.1以上版本的新特性,工厂类目录，其实就是用来批量填充测试数据
    
    - ModelFactory.php 可以自定义不同model所需要的数据类型
  
  - migrations 存储数据库迁移文件的目录  
  - seeds   存放数据填充类的目录
    
    - DatabaseSeed.php 执行php artisan db:seed将会调用该类的run方法,该方法可以调用该目录下其他的seed类

- public  网站入口,应当将ip或者域名指向该目录,可供外部访问的css,js和图片也放在这个目录

  - index.php 入口文件
  - .htaccess apache服务器用该文件重写url
  -  IIS服务器用该文件重写url

resources  资源文件目录
  
  - assets 可存放包含less,sass等原始资源目录
  - lang本地化文件目录
  - views 视图文件存放目录
  
storage  存储目录,web服务器需要有该目录的写入权限
  
  - app 可用于存储应用程序需要的一些文件
  - framwork 该目录包含缓存,session和编译后的视图文件
  - logs 日志目录

- tests 测试目录
- vendor 该目录包含laravel源代码和第三方依赖包\
-  .env 环境配置文件
- artian 强大的命令行接口,可以在app/Console/Commands下自定义编写命令
- composer.json 存放依赖关系的文件
- composer.lock 锁文件,存放安装是依赖包的真实版本
- gulpfile.js gulp(一种前端构建构建)的配置文件
- package.json   gulp配置文件
- phpspec.yml 一种测试框架配置文件
- phpunit.xml 一种测试框架配置文件
- server.php  php内置服务器

