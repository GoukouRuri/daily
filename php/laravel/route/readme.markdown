* 不同版本使用不同路由组
```php
Route::namespace('Api\v1')->group(function () {
    Route::any("/", 'HomeController@index'); 
    Route::any("/login/login", 'LoginController@login'); 
});
```