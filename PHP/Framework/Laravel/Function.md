### 常用的函数使用方法

* 如何加载自己定义的类库和函数呢？

  - autoload加files定义自动加载路径后执行composer dump-autoload
  ```
  "autoload": {
     "classmap": [
        "database"
     ],
     "psr-4": {
         "App\\": "app/"
     },
     "files": [
         "app/tools/helpers.php"
     ]
  }
  ```