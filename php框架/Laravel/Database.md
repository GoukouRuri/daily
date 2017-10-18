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
    
  - 原生sql使用
   
  - DB类连接、查询构造器使用
    
    - 查询语句 
  
    ```php
    <?php
    // 获取所有行(返回的是对象组成的数组)
    $users = DB::table('user')->get();
    // 或者也可以根据条件获取多行
    $users = DB::table('user')->where('user_id', '=' ,1)->get();
    foreach ($users as $user) {
        echo $user->name;
    }

    // 获取单条数据(返回一个对象)
    $user = DB::table('users')->where('name', 'John')->first();
    echo $user->name;

    /*------不想获取整行数据,只想取某列的值怎么办------*/
    // 只获取单条数据中的某列
    $email = DB::table('users')->where('name', 'John')->value('email');
    echo $email;

    // 只获取多行数据的单列
    $titles = DB::table('roles')->pluck('title');
    foreach ($titles as $title) {
        echo $title;
    }

    // 只获取多行数据的两列(返回数据, 第一个参数为值, 第二个为键,参数最多两个)
    $roles = DB::table('roles')->pluck('title', 'name');
    //$roles = DB::table('roles')->lists('title', 'name');
    foreach ($roles as $name => $title) {
        echo $title;
    }
    
    // 那么如何获取自己指定的列呢,需要用select()指定
    $users = DB::table('users')->select('name', 'email as user_email')->get();
    // 如果已经有了还想加怎么办
    $users = $users->addSelect('age')->get(); 
    
    // 分块查询
    DB::table('users')->orderBy('id')->chunk(100, function ($users) {
        // Process the records...
    
        return false; //返回false来阻止进一步处理的块Closure
    });

    // 复合函数count，max，min，avg，和sum

    $users = DB::table('users')->count();
    $price = DB::table('orders')->max('price');
    $users = DB::table('users')->distinct()->get();

    // 如何配合原始的sql语句来查询呢, 用DB::raw()可以防止sql注入
    $users = DB::table('users')
        ->select(DB::raw('count(*) as user_count, status'))
        ->where('status', '<>', 1)
        ->groupBy('status')
        ->get();

    /*------联表查询如何使用------*/
    // 内联join ,inner join, 第一个参数为联的表,后面参数为联表的相关字段约束
    $users = DB::table('users')
                ->join('contacts', 'users.id', '=', 'contacts.user_id')
                ->join('orders', 'users.id', '=', 'orders.user_id')
                ->select('users.*', 'contacts.phone', 'orders.price')
                ->get();

    // 外联中的左联, 第一个参数为联的表,后面参数为联表的相关字段约束
    $users = DB::table('users')->leftJoin('posts', 'users.id', '=', 'posts.user_id')->get();

    // 联表约束匿名函数化写法
    DB::table('users')->join('contacts', function ($join) {
        $join->on('users.id', '=', 'contacts.user_id')->where('contacts.user_id', '>', 5);
    })->get();

    // 联合查询
    $first = DB::table('users')
        ->whereNull('first_name');
    
    $users = DB::table('users')
        ->whereNull('last_name')
        ->union($first)
        ->get();

    
    /*------多种where条件语句------*/
    // where
    $users = DB::table('users')
        ->where('votes', '>=', 100)
        ->get();
    
    $users = DB::table('users')
        ->where('votes', '<>', 100)
        ->get();
    
    $users = DB::table('users')
        ->where('name', 'like', 'T%')
        ->get();

    $users = DB::table('users')->where([
        ['status', '=', '1'],
        ['subscribed', '<>', '1'],
    ])->get();  // 传入数组条件, 但是需要是二维数组形式

    // orWhere, whereBetween, whereNotBetween, whereIn, whereNotIn, whereNull, whereNotNull
    $users = DB::table('users')
        ->where('votes', '>', 100)
        ->orWhere('name', 'John')
        ->get();

    // 比较时间whereDate, whereMonth, whereDay, whereYear
    $users = DB::table('users')
        ->whereDate('created_at', '2016-12-31')
        ->get();

    $users = DB::table('users')
        ->whereMonth('created_at', '12')
        ->get();

    // whereColumn方法可用于验证两列是否相等或者比较
    $users = DB::table('users')
        ->whereColumn('first_name', 'last_name')
        ->get();
    $users = DB::table('users')
        ->whereColumn('updated_at', '>', 'created_at')
        ->get();
    // whereColumn方法也可以传递多个条件的数组。这些条件将使用and运算符进行连接
    $users = DB::table('users')
        ->whereColumn([
            ['first_name', '=', 'last_name'],
            ['updated_at', '>', 'created_at']
        ])->get();

    // 组合条件
    DB::table('users')
        ->where('name', '=', 'John')
        ->orWhere(function ($query) {
            $query->where('votes', '>', 100)
                  ->where('title', '<>', 'Admin');
        })
        ->get();
    // 等效为select * from users where name = 'John' or (votes > 100 and title <> 'Admin')

    // where从句
    DB::table('users')
        ->whereExists(function ($query) {
            $query->select(DB::raw(1))
                  ->from('orders')
                  ->whereRaw('orders.user_id = users.id');
        })
        ->get();
    // 等效为select * from users where exists (select 1 from orders where orders.user_id = users.id)

    // JSON where where子句(需要mysql5.7以上)

    // 排序, 第一个为字段名, 第二个为asc或者desc
    $users = DB::table('users')
        ->orderBy('name', 'desc')
        ->get();

    // 组查询groupby, having
    $users = DB::table('users')
        ->groupBy('account_id')
        ->having('account_id', '>', 100)
        ->get();
    // havingRaw方法可用于将原始字符串设置为having子句的值, 下面是查取销售额超过$ 2,500的所有部门
    $users = DB::table('orders')
        ->select('department', DB::raw('SUM(price) as total_sales'))
        ->groupBy('department')
        ->havingRaw('SUM(price) > 2500')
        ->get();

    // 分段取数据
    $users = DB::table('users')->skip(10)->take(5)->get();  //跳过10个开始取5个
    // 或者用
    $users = DB::table('users')->offset(10)->limit(5)->get();

    // 条件条款--有时候，只有当其他的事情都是真的时，你可能会希望子句才能应用于查询。例如，where如果传入请求中存在给定的输入值，则可能只需应用语句。您可以使用以下when方法完成此操作
    $role = $request->input('role');
    $users = DB::table('users')
        ->when($role, function ($query) use ($role) {
            return $query->where('role_id', $role);
        })
        ->get();   //该when方法仅在第一个参数时执行给定的Closure true。如果第一个参数是false，Closure将不会被执行
    // 或者第三个参数为匿名函数, 在第二个不执行的情况下的默认回调动作
    $sortBy = null;
    
    $users = DB::table('users')
        ->when($sortBy, function ($query) use ($sortBy) {
            return $query->orderBy($sortBy);
        }, function ($query) {
            return $query->orderBy('name');
        })
        ->get();
    ```
    
    - 插入语句
    ```php
    <?php
    // insert方法接受列名和值的数组
    DB::table('users')->insert(
        ['email' => 'john@example.com', 'votes' => 0]
    );
    
    // 批量插入, insert接受二维数组
    DB::table('users')->insert([
        ['email' => 'taylor@example.com', 'votes' => 0],
        ['email' => 'dayle@example.com', 'votes' => 0]
    ]);
    
    // 如果表有自增的主键,可以获取成功插入一条数据后的主键
    $id = DB::table('users')->insertGetId(
        ['email' => 'john@example.com', 'votes' => 0]
    );
    ```
    
    - 更新语句
    ```php
    <?php
    // update方法与insert方法一样，接受包含要更新的列的列和值对的数组。您可以update使用where子句约束查询
    DB::table('users')
        ->where('id', 1)
        ->update(['votes' => 1]);

    // 快速递增和递减(限制int类型字段)
    DB::table('users')->increment('votes');
    DB::table('users')->increment('votes', 5);
    DB::table('users')->decrement('votes');
    DB::table('users')->decrement('votes', 5);
    // 也可以在快速操作时更新其他的列
    DB::table('users')->increment('votes', 1, ['name' => 'John']); 
    
    ```
    
    - 删除语句
    ```php
    <?php
    // 查询构建器也可以用于通过该delete方法从表中删除记录。您可以delete通过where在调用delete方法之前添加子句来约束语句
    DB::table('users')->where('votes', '>', 100)->delete();

    // 如果是清空整个表的话, 请使用truncate()
    DB::table('users')->truncate();
    ```
    
    - [分页查询](https://laravel.com/docs/5.5/pagination)
    ```php
    <?php
    $users = DB::table('users')->paginate(15);
 
    //分页实例方法, 每个分页器实例通过以下方法提供其他分页信息：
    $results->count();
    $results->currentPage();
    $results->firstItem();
    $results->hasMorePages();
    $results->lastItem();
    $results->lastPage(); //(Not available when using simplePaginate)
    $results->nextPageUrl();
    $results->perPage();
    $results->previousPageUrl();
    $results->total(); //(Not available when using simplePaginate)
    $results->url($page);
    
    ```
    - [Redis](https://laravel.com/docs/5.5/redis)
  
    ```php
    <?php
    // 实例化一个redis实例
    $redis = Redis::connection();

    // 或者是直接操作Redis的Fader
    ```    
    