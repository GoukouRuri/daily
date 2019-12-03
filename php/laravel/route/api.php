<?php
// api路由常见配置


// 不同版本不同路由组
Route::namespace('Api\v1')->group(function () {
	Route::any("/", 'HomeController@index'); 
	Route::any("/login/login", 'LoginController@login'); 
});





