> ### Jquery对象和DOM对象

* DOM(document object model)是文档对象模型,每一份DOM构成DOM树
* Jquery对象通过jquery包装DOM对象之后产生的对象
  
  - example:
  
    `$("#foo").html();`  jquery对象是jquery独有的,$("#foo")为jqeury对象,如果是jquery对象就可以使用jquery里的方法了,但无法使用DOM里的任何方法
    
    `document.getElementById("foo").innerHtml();`  DOM对象无法使用jquery里的方法
    
* jquery对象和DOM对象相互转化

  - 定义变量
  
    - var $variable = Jquery对象;
    - var variable =  DOM对象;
    
  - jquery对象是个数组对象,与dom对象有以下方式转换
  
    - jquery对象转为dom对象
    ```var $cr = $("#cr");            // jquery对象
       var cr = $cr[0];               // dom对象
    ```
    - jquery对象转为dom对象
    ```
       var $cr = $("#cr");            // jquery对象
       var cr = $cr.get(0);               // dom对象
    ```
    - dom对象转为jquery对象
    ```
       var cr = document.getElementById("cr");          // dom对象
       var $cr = $(cr);                              // jquery对象
    ```
    
> ### 解决jquery库和其他库

* jquery库所有的插件都限制在它自己的命名空间中,不会和其他冲突,只有快捷方式`$`会出现冲突

  - jquery库在其他库之后加载
  
   `jQuery.noConflict();`   // 将$移交给其他库，jquery则使用jQeury来引用自身
   
  - 其他库在jquery之后加载
  
    $已经在其他库时，jquery则使用jQeury来引用自身
    
> ### jquery中的DOM操作

* 分类
  - DOM Core
  - Html-Dom 
  - Css-Dom 
  
* 节点
  - 创建元素节点、文本节点和属性节点
  ```
  var li_1 = $('<li title="香蕉">创建第一个li元素</li>');          //<li></li>为元素节点,'创建第一个li元素'为文本节点，title="香蕉"为属性节点
  var li_2 = $('<li>创建第二个li元素</li>');
  $('ul').append(li_1).append(li_2);  //链式插入li元素
  ```
  
  - 插入节点
  
    - [append()](http://jquery.cuishifeng.cn/append.html)  向每个匹配的元素内部追加内容 
    - [appendTo()](http://jquery.cuishifeng.cn/appendTo.html)  append的反操作
    - [prepend()](http://jquery.cuishifeng.cn/prepend.html)     向每个匹配的元素内部前置内容
    - [prependTo()](http://jquery.cuishifeng.cn/prependTo.html)   prependTo的反操作
    - [after()](http://jquery.cuishifeng.cn/after.html)     向每个匹配的元素之后添加元素
    - [insertAfter()](http://jquery.cuishifeng.cn/insertAfter.html)     after的反操作
    - [before()](http://jquery.cuishifeng.cn/before.html)            向每个匹配的元素之前添加元素
    - [insertBefore()](http://jquery.cuishifeng.cn/insertBefore.html)     before的反操作
  
  - 删除节点
  
    - [remove()](http://jquery.cuishifeng.cn/remove.html)   删除每个匹配的节点
    - [empty()](http://jquery.cuishifeng.cn/empty.html)    清空每个匹配的节点的内容和子节点
    
  - 复制节点
  - 替换节点
  - 包裹节点
  - 遍历节点(children().find().child().parent(),parents(),filter(),nextAll(),prev(),next(),prev
  all(),siblings(),closest())

* 属性

  - 获取和设置属性(attr())
  - 删除属性(removeAttr())

* 样式
  
  - 获取和设置样式(attr()),将原来的替换成新的class
  ```
  <p class="oldclass"></p>
  $('p').attr('class', 'newclass');
  ```
  
  - 追加样式(addClass())
  - 移除样式(removeClass())
  - 是否有样式(hasClass())
  
* CSS-DOM操作(css(),height().width(),offset().position(),scrollTop,scrollLeft())

> ### jquery事件和动画

* 绑定事件bind()
* 合成事件toggle(),hover()
* 事件冒泡
  
  - 多个元素绑定同一类型事件,并且元素之间是嵌套关系，则触发顺序从里到外
 

  
