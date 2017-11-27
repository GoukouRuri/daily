* 出错`SQLSTATE[HY000]: General error: 1364 Field 'phone' doesn't have a default value (SQL: insert into `t_users` (`name`, `email`, `password`, `updated_at`, `created_at`) values (admin, 547648730@qq.com, $2y$10$3n/c2TZ2TPSk3SYBdqKxu.Oz1qJwVdlT.1LzargnpGKvviCMXhKbG, 2017-10-18 09:50:16, 2017-10-18 09:50:16))`

  - Model 中 $fillable 未加入该字段或者字段未设置默认值
  
* php artisan migrate时出现错误`[Illuminate\Database\QueryException]
                           SQLSTATE[42000]: Syntax error or access violation: 1071 Specified key was too long; max key length is 767 bytes (SQL: alter table users add unique users_email_unique(email))`
                           
  - 手动配置迁移命令migrate生成的默认字符串长度，在AppServiceProvider中调用Schema::defaultStringLength方法来实现配置：
   `Schema::defaultStringLength(191);`
   
  - 或者升级mysql到5.7版本及以上















