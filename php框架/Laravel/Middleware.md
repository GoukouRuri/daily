### 中间件的配置和使用
- Http/Kernel.php配置中间件

- web中间件(route.php默认会引入这个中间件)
  
  - csrf和session的启用
  
- 全局的中间件

- 路由里配置的中间件

  - 可以自己在```protected $routeMiddleware```中自定义中间件
  - ```php artian make:middleware [AdminLogin]``` 生成中间件