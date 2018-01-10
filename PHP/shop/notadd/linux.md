## 系统环境
  
  centos6.9
  
  修改系统为中文显示
```sh
echo $LANG #查看系统当前使用的字符集
vim /etc/sysconfig/i18n    #更改字符集所在的配置文件，使用#号注释掉之前的英文字符集，重新添加一行LANG=zh_CN.utf8。
source /etc/sysconfig/i18n  #执行这条命令，让前面的修改生效。
echo $LANG  #查看当前字符集是否已经修改成功
如果只是临时调整，可以使用命令LANG=en，临时调整在登录注销重新登录后就会消失。
```