> ### For Windows System

### 安装(必须有java环境,tomcat不是必要的,可以tomcat服务器部署也可以不用(如果用需要tomcat6以上版本,端口一般为tomcat的8080端口),solr自带服务器(端口默认8983))

  - solr自带服务器部署(建议新手用这个)
  
    - http://leil.plmeizi.com/archives/apache-solr%E4%BD%BF%E7%94%A8%E7%AE%80%E4%BB%8B/
    - 替换solrconfig.xml(关于id的int类型定义等配置)
    - 在schema.xml基础上添加修改字段和权重字段
    
  - tomcat服务器上部署(自行google,有许多未知的坑和配置,比较复杂)
  
    - http://blog.csdn.net/zhangt85/article/details/41483759

### php操作solr

  - php文件包方式查询方法
  
    - http://blog.csdn.net/jiangchao858/article/details/53571985
    - http://haiziwoainixx.iteye.com/blog/2095599
    - http://blog.csdn.net/qq_19244423/article/details/48159945
    - http://blog.csdn.net/wuzhilon88/article/details/42675573
    