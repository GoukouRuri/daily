* 出错`SQLSTATE[HY000]: General error: 1364 Field 'phone' doesn't have a default value (SQL: insert into `t_users` (`name`, `email`, `password`, `updated_at`, `created_at`) values (admin, 547648730@qq.com, $2y$10$3n/c2TZ2TPSk3SYBdqKxu.Oz1qJwVdlT.1LzargnpGKvviCMXhKbG, 2017-10-18 09:50:16, 2017-10-18 09:50:16))`

  - Model 中 $fillable 未加入该字段或者字段未设置默认值
















