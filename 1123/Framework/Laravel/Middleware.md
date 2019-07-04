### 中间件的配置和使用
- Http/Kernel.php配置中间件

- web中间件(route.php默认会引入这个中间件)
  
  - csrf和session的启用

- guest中间件对应默认的RedirectIfAuthenticated
  
- 全局的中间件

- 路由里配置的中间件

  - 可以自己在app/Http/Kernel.php文件里的```protected $routeMiddleware```中自定义中间件
  - ```php artian make:middleware [AdminLogin]``` 生成中间件
  - 常用代码

   ```php
   <?php

   /*if (!Auth::user()) {
        return redirect()->guest('admin/login');
    }*/
	/*if (!Auth::user()->hasPermission(Route::currentRouteName()) && !SiteUtils::isSuperAdmin()) {
        return redirect()->route("admin.index.index")->withErrors("没有操作权限");
    }*/

    if (Auth::guest()) {
        if ($request->ajax()) {
            return response('Unauthorized!', 401);
        } else {
            return redirect()->guest('admin/login');
        }
    }

    view()->share('auth.loign', true);
   ```