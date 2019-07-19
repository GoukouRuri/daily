### php配置项修改

* 平时修改php.ini里配置即可，有些比较特殊,有独特的配置文件会复写， 例如对php开启的opcache相关参数的修改

ex:
```shell
$ php -i | grep opcache
```
查看具体的配置加载项加载情况进行修改


