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