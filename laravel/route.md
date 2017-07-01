### 路由基本格式 

- 命名路由
  - 命名路由让你可以更方便的为特定路由生成 URL 或进行重定向。你可以使用 as 数组键指定名称到路由上：

      ```
      Route::get('login', ['as' => 'admin.login', function () {
          // echo route('admin.login'); 路由的别名
      }]);
      ```
  
  - 还可以指定路由名称到控制器动作：
        
      ```
      Route::get('login', [
          'as' => 'login',
          'uses' => 'UserController@login'
      ]);
      ```
      
  - 除了可以在路由的数组定义中指定路由名称外，你也可以在路由定义后方链式调用 name 方法：
    
      ```
      Route::get('login', 'UserController@login')->name('login');
      ```
      
- 分组路由 ------十分重要
  
  ```
  Route::group(['prefix' =>'admin', 'namesapce' => 'Admin', 'middleware' => ['web', 'admin.login'], 'domain' => '{domain}.sample.app'], function () {
     Route::get('dashboard', ['as' => 'admin.dashboard', function ($domain) {
         // prefix:路由前缀,namespace：命名空间,middleware:中间件,domail:子域名
     }]);
  });
  ```
  
- 资源路由/

  ```
  Route::resource('article','ArticlesController')->name('article');
  ```
  等同于下面路由
  ```
  方式           路径                   行为  路由名称          作用
  GET           /article               索引 article.index     文章列表
  GET           /article/create        创建 article.create    新增一篇文章
  POST          /article               保存 article.store     保存提交的表单
  GET           /article/{id}          显示 article.show      显示一篇文章
  GET           /article/{id}/edit     编辑 article.edit      编辑一篇文章
  PUT/PATCH     /article/{id}          更新 article.update    修改/更新一篇文章
  DELETE        /article/{id}          删除 article.destroy   删除一篇文章
  ```
  
- 正则表达式限制参数

  你可以使用 where 方法来限制路由参数格式。where 方法接受参数的名称和定义参数应该如何被限制的正则表达式：
  
  ```
  Route::get('user/{id}', function ($id) {
      //
  })->where('id', '[0-9]+');
  
  Route::get('user/{name}', function ($name) {
      //
  })->where('name', '[A-Za-z]+');
  Route::get('user/{id}/{name}', function ($id, $name) {
      //
  })->where(['id' => '[0-9]+', 'name' => '[a-z]+']);
  ```
  如果你希望路由参数可以总是遵循正则表达式，则可以使用 pattern 方法。你应该在  RouteServiceProvider 的 boot 方法里定义这些模式：
  ```
  public function boot(Router $router)
  {
     $router->pattern('id', '[0-9]+');
     parent::boot($router);
  }
  ```
  
- 对命名路由生成 URLs

  一旦你在指定的路由中分配了名称，则可通过 route 函数来使用路由名称生成 URLs 或重定位：
  ```
  $url = route('profile');
  $redirect = redirect()->route('profile');
  ```
  如果路由定义了参数，那么你可以把参数作为第二个参数传递给 route 方法。指定的参数将自动加入到 URL 中：
  ```
  Route::get('user/{id}/profile', ['as' => 'profile', function ($id) {
      //
  }]);
  $url = route('profile', ['id' => 1]);
  ```
  
- 路由模型绑定[https://docs.golaravel.com/docs/5.1/routing/]

  Laravel 路由模型绑定提供了一个方便的方式来注入类实例到你的路由中。例如，除了注入一个用户的 ID，你也可以注入与指定 ID 相符的完整 User 类实例。
  
  首先，使用路由的 model 方法为指定参数指定类。必须在 RouteServiceProvider::boot 方法中定义你的模型绑定：
  
  绑定参数至模型
  
  ```
  public function boot(Router $router)
  {
     parent::boot($router);
     
     $router->model('user', 'App\User');
  }
  ```
  接着，定义包含 {user} 参数的路由：
  
  ```
  $router->get('profile/{user}', function(App\User $user) {
     //
  });```
  
- CSRF 保护[https://docs.golaravel.com/docs/5.1/routing/]