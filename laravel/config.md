### 配置项设置和读取

- config函数

  example:
  
  ```
  config(database.connections.mysql.prefix);
  config(app.debug);
  ```
  
- .env文件抽离配置项,不提交版本控制,方便各种配置独立的开发环境