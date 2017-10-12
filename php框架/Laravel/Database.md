### Eloquent的使用(orm模型操作数据库)[https://docs.golaravel.com/docs/5.1/eloquent-collections/]

  - 生成模型（如果是放在model目录里,需要修稿config目录的service.php文件里的路径）
  
    ```php artian make:model Models/Article -m```  同时会生成模型和migration迁移文件
  
  - 生成迁移文件
  
    `php artisan make:migration create_users_table --create=users`
    `php artisan make:migration add_votes_to_users_table --table=users`
  - model文件里的配置[https://docs.golaravel.com/docs/5.1/eloquent/]
  
    ```
    protected $table = "user";" // 绑定相关的表
    protected $primaryKey = "user_id"; // 绑定主键
    public $timestamps = false; //关闭自动更新时间戳,一般都是开启
    
    ```
    
  - 使用方法
  
    ```
    $user = User::where('user_id', 1)->get();
    $user = User::find(1); 
    $user->user_name = 'paul';
    $user->update();
    ```
    
### Eloquent模型约定[http://laravelacademy.org/post/130.html]

  - 默认规则是模型类名的复数作为与其对应的表名，除非在模型类中明确指定了其它名称。所以，在本例中，Eloquent认为Flight模型存储记录在Users表中。你也可以在模型中定义table属性来指定自定义的表名(如果定义了前缀不需要加，会自动带入前缀)
    
    ```php artisan migrate``` 通过迁移生成或者更新表
    
    ```php artisan migrate --force``` 强制更新表
    
    ```php artisan migrate:rollback``` 回滚最新的一次迁移操作
    
    ```php artisan migrate:reset``` 回滚所有迁移操作
    
    ```
    php artisan migrate:refresh
    php artisan migrate:refresh --seed
    ```回滚所有迁移操作，重新执行迁移
    
### 监控查询事件[https://laravel.com/docs/5.5/database]  

  - 如果要接收应用程序执行的每个SQL查询，可以使用该listen方法。此方法对于记录查询或调试很有用。您可以在服务提供商中注册您的查询监听器
  
### 自动事务和手动事务处理[https://laravel.com/docs/5.5/database]

### 数据库操作[https://docs.golaravel.com/docs/5.1/queries/]

  - pdo连接
  
    ```$pdo = DB::connection()->getPdo();```
    
  - DB类连接
  
    ```$users = DB::table('user')->where('user_id', '=' ,1)->get();```