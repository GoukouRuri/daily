### 配置项设置和读取

- config函数

  example:
  
  ```
  config(database.connections.mysql.prefix);
  config(app.debug);
  ```
  
- .env文件抽离配置项,不提交版本控制,方便各种配置独立的开发环境

- 不想在一些路由使用表单加csrf token验证

  `app/Http/Middleware/VerifyCsrfToken.php`目录的protected $except = []中加入忽略的路由匹配规则