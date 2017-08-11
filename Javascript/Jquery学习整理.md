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