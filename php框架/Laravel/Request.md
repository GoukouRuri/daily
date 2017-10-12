### Request表单验证[http://www.cnblogs.com/php-linux/p/6002672.html]

* 在项目目录下使用artisan的make:request命令就可以生成一个用于表单验证Request类
 
   ```php artisan make:request StoreArticleRequest```
   
* 实现验证

   - 这个命令生成的文件位于app/Http/Requests/这个文件夹当中,可以看到里面会有两个方法：authorize()和 rules()

  