### phpstorm食用指南

  - 官网手册地址https://www.jetbrains.com/help/phpstorm/configuring-line-separators.html#separator_settings
  
  - 参考整理来源http://blog.csdn.net/u012906135/article/details/48130801

* 主题的安装for windows
   - config/colors下放置主题文件
* 关闭右上方四个浏览器图标
   - settings->tools->web browsers
* 关闭右侧那根指示线
   - settings->editor->general->apperarnce->show right margin
* tab缩进设置为四个空格
   - settings->editor->code style
* 关闭和开启新版本的参数提示
   - settings->editor->apperarnce->show parameter name himts
* 代码自动换行开启和关闭
   - settings->editor->general->Use soft wrap in editor
* 从索引mask中排除文件
   - settings->editor->file types
   - 个人的使用的过滤规则

     ```
     
      *.bmp;*.css;*.eot;*.fla;*.gif;*.hprof;*.jpg;*.png;*.pyc;*.pyo;*.rbc;*.swf;*.ttf;*.woff;*.zip;*2013;*2014;*~;.DS_Store;.git;.hg;.svn;CVS;RCS;SCCS;__pycache__;_svn;adtest;batch;bin;cache;css;csssprite;doc;docs;flash;font;fonts;gmap;icon;image;images;inc;js;log;logs;oa_login;openads;pear;player;qqMaps;rcs;scripts;style;test;tools;touch;upload;uploads;

     ```

* 添加版本控制忽略的文件--也可以自己写入规则进行忽略
    - settings->version control->ignored files

* 常用的搜索快捷键
    - 搜索文件-----------快速连按两次shift键
    - 全局搜素文件--------shift+ctrl+alt+N
    - 搜索匹配的内容-------shift+ctrl+F
    - 全项目范围查找类--------------ctrl+N
    - 查取函数或类在哪些地方被调用---alt+f7
    - 查取最近打开的文件------------ctrl+e
    - 查看类的继承关系-------------[Show Diagram](https://laravel-china.org/topics/3187/how-to-use-phpstorm-to-view-class-inheritance-relationships)
* 常用的提示快捷键
    - ctrl+J-------------代码提示
    - ctrl+P-------------方法参数提示
    - ctrl+alt+space-----类名和接口提示
    - ctrl+alt+A---------查看快捷键
    - ctrl+alt+B---------找到继承该接口或者父级 的所有子类, 统计所有子类个数
    - ctrl+O-------------查看魔术方法
    - ctrl+D-------------复制光标所在当前的行
    - ctrl+W-------------复制光标所在的区域,连续按会继续扩大范围
    - ctrl+alt+L---------快速格式化代码
    - ctrl+alt+O---------优化导入的类
    - ctrl+alt+左方向键---退回到上一个操作
    - ctrl+alt+右方向键---前进到下一个操作
    - ctrl+shift+enter---自动补全末尾分号结尾
    - F2-----------------跳转到下一个错误和高亮的位置
    - ctrl+alt+U---------单词大小写转换
    - ctrl+N-------------快速查找类
    - ctrl+shift+alt+N---快速查找函数
    - ctrl+shift+N-------快速查找文件
    - ctrl+G-------------跳转到指定的行处
* 常用的文件操作快捷键
    - F5 复制文件
    - F6 移动文件
    - Alt + Delete 安全删除
    - Shift + F6 为所选文件重命名
    - pin tab 将文件标签固定
    
* 激活码`http://blog.csdn.net/u013939884/article/details/68921462`
  http://www.0-php.com:1017
