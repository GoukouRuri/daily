* 创建中间件命令
```shell
php artisan make:middleware CheckAge
```

* 中间件全局配置文件
```text
app/Http/Kernel.php
```

* 在配置中定义中间件
```php
// Within App\Http\Kernel Class...

// 定义中间件
protected $routeMiddleware = [
    'auth' => \App\Http\Middleware\Authenticate::class,
    'auth.basic' => \Illuminate\Auth\Middleware\AuthenticateWithBasicAuth::class,
    'bindings' => \Illuminate\Routing\Middleware\SubstituteBindings::class,
    'cache.headers' => \Illuminate\Http\Middleware\SetCacheHeaders::class,
    'can' => \Illuminate\Auth\Middleware\Authorize::class,
    'guest' => \App\Http\Middleware\RedirectIfAuthenticated::class,
    'signed' => \Illuminate\Routing\Middleware\ValidateSignature::class,
    'throttle' => \Illuminate\Routing\Middleware\ThrottleRequests::class,
    'verified' => \Illuminate\Auth\Middleware\EnsureEmailIsVerified::class,
];

// 设置中间件执行的优先级(哪些先执行, 很少用到, 除非是多个中间件必须按规定顺序执行)
protected $middlewarePriority = [
    \Illuminate\Session\Middleware\StartSession::class,
    \Illuminate\View\Middleware\ShareErrorsFromSession::class,
    \App\Http\Middleware\Authenticate::class,
    \Illuminate\Session\Middleware\AuthenticateSession::class,
    \Illuminate\Routing\Middleware\SubstituteBindings::class,
    \Illuminate\Auth\Middleware\Authorize::class,
];
```

* 在路由中采用配置中定义好的中间件
```php
Route::get('admin/profile', function () {
    //
})->middleware('auth');

Route::get('/', function () {
    //
})->middleware('first', 'second');
```

* 也可以不在配置中定义, 可以直接使用中间件文件
```php
use App\Http\Middleware\CheckAge;

Route::get('admin/profile', function () {
    //
})->middleware(CheckAge::class);
```

* 中间件传参
```php
// 在定义路由时，可以通过使用分隔中间件名称和参数来指定中间件参数:。多个参数应以逗号分隔：
Route::put('post/{id}', function ($id) {
    //
})->middleware('role:editor');

// 在中间文件中传参$role
public function handle($request, Closure $next, $role)
{
    if (! $request->user()->hasRole($role)) {
        // Redirect...
    }

    return $next($request);
}
```

* 终止中间件
```php
// 在中间文件中定义方法terminate
public function terminate($request, $response)
{
    // Store the session data...
}
```

* 中间件中可以将路由转发
```php
// laravel使用Request::create和Route::dispatch($request), 尽量不要使用replace()替换参数
$request = Request::create('games/result', 'POST', array(
     "name"     => Session::get('name'),
     "score"    => Session::get('score'),
     "Level"    => Session::get('Level'),
     "accuracy" => Session::get('accuracy'), 
     "time"     => Session::get('time'),
     "bouns"    => Session::get('bouns')
));           
$response = Route::dispatch($request);
return $response;
```















