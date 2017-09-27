# What is Panshi?

Panshi is an open source, [object oriented](http://en.wikipedia.org/wiki/Object-oriented_programming) [MVC](http://en.wikipedia.org/wiki/Model–view–controller "Model View Controller") [web framework](http://en.wikipedia.org/wiki/Web_application_framework) built using [PHP5](http://php.net/manual/intro-whatis "PHP Hypertext Preprocessor") by a team of volunteers that aims to be swift, secure, and small.

[!!] Panshi is licensed under a [BSD license](http://Panshiframework.org/license), so you can legally use it for any kind of open source, commercial, or personal project.

## What makes Panshi great?

Anything can be extended using the unique [filesystem](files) design, little or no [configuration](config) is necessary, [error handling](errors) helps locate the source of errors quickly, and [debugging](debugging) and [profiling](profiling) provide insight into the application.

To help secure your applications, tools for [input validation](security/validation), [signed cookies](security/cookies), [form] and [HTML] generators are all included. The [database](security/database) layer provides protection against [SQL injection](http://wikipedia.org/wiki/SQL_injection). Of course, all official code is carefully written and reviewed for security.

## Contribute to the Documentation

We are working very hard to provide complete documentation. To help improve the guide, please [fork the userguide](http://github.com/Panshi/userguide), make your changes, and send a pull request. If you are not familiar with Git, you can also submit a [feature request](http://dev.Panshiframework.org/projects/Panshi3/issues) (requires registration).

## Unofficial Documentation

If you are having trouble finding an answer here, have a look through the [unofficial wiki](http://kerkness.ca/kowiki/doku.php). Your answer may also be found by searching the [forum](http://forum.Panshiframework.org/) or [Stack Overflow](http://stackoverflow.com/questions/tagged/Panshi) followed by asking your question on either.  Additionally, you can chat with the community of developers on the freenode [#Panshi](irc://irc.freenode.net/Panshi) IRC channel.

> ### Kohana3框架简单入门  -- 非官方版本

***

* 目录结构

  - 入口文件  index.php
  
    - 设置application,module,cache,log,system等路径
    
      - 根目录:  `../app`
      - 加载的应用配置文件  `../app/config/app.php`
      - 框架模块目录     `../../framework/modules`
      - 框架系统目录     `../../framework/system`
      - 缓存目录         `cache`
      - log目录          `logs`
      - 跨域设置
      - 加载引导文件bootstrap.php      `../app/bootstrap.php`  
      - 设置Error reporting的等级
      - 最后一段代码判断是php的运行模式是cgi还是fpm-fcgi模式,现在基本上都是后者,下面是index.php结束后进行路由分发
        
        ```php
         echo Request::factory(TRUE, array(), FALSE)    //生成实例
             ->execute()                                //执行,其中进行了分发,调用了controller
             ->send_headers(TRUE)                       //给定头部
             ->body();                                  //得到request的一些参数
        ```
        