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