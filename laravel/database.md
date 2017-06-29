### 数据库操作[https://docs.golaravel.com/docs/5.1/queries/]

  - pdo连接
  
    ```$pdo = DB::connection()->getPdo();```
    
  - DB类连接
  
    ```$users = DB::table('user')->where('user_id', '=' ,1)->get();```
    
### Eloquent的使用(orm模型操作数据库)[https://docs.golaravel.com/docs/5.1/eloquent-collections/]

  - 生成模型
  
    ```php artian make:model [model_name]```
    
  - model文件里的配置[https://docs.golaravel.com/docs/5.1/eloquent/]
  
    ```
    protected $table = "user";" // 绑定相关的表
    protected $primaryKey = "user_id"; // 绑定主键
    public $timestamps = false; //关闭自动更新时间戳,一般都是开启
    
    ```
    
  - 使用方法
  
    ```$user = User::where('user_id', 1)->get();```
    
    ```
    $user = User::find(1); 
    $user->user_name = 'paul';
    $user->update();
    
    ```