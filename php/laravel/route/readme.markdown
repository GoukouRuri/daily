* 不同版本使用不同路由组
```php
Route::namespace('Api\v1')->group(function () {
    Route::any("/", 'HomeController@index'); 
    Route::any("/login/login", 'LoginController@login'); 
});
```

* 可用的路由器方法
```php
Route::get($uri, $callback);
Route::post($uri, $callback);
Route::put($uri, $callback);
Route::patch($uri, $callback);
Route::delete($uri, $callback);
Route::options($uri, $callback);

Route::get('foo', function () {
    return 'Hello World';
});
Route::get('/user', 'UserController@index');
Route::get('user/{id}', function ($id) {
    return 'User '.$id;
});
Route::get('posts/{post}/comments/{comment}', function ($postId, $commentId) {
    //
});
Route::match(['get', 'post'], '/', function () {
    // 匹配get、post请求
});
Route::any('foo', function () {
    // 匹配任意类型请求
});
```

* 重定向路由
```php
Route::redirect('/here', '/there');
```

* 为路由命名
```php
Route::get('user/profile', 'UserProfileController@show')->name('profile');
```

* 路由前缀和命名空间
```php
Route::prefix('admin')->group(function () {
    Route::get('users', function () {
        // Matches The "/admin/users" URL
    });
});
```










