### 虚拟机操作[http://www.cnblogs.com/xghb/p/4904146.html]

  - Homestead 目录下
  
    1. 开机： vagrant up
    2. 关机： vagrant halt
    3. 销毁： vagrant destroy --force
    4. 登录:  vagrant ssh
    
  - 访问网站
  
    - hosts配置dns
      
       192.168.10.10 sample.app
       
    -  访问http://.app
    
  - SSH登录
  
    - 通过ssh登录 ssh vagrant@127.0.0.1 -p 2222
    
  - 连接虚拟机内Mysql
  
    - mysql -h 127.0.0.1:33060 -u homestead -p secret
    
  - 增加站点
  
    - 方式一
      
      Homestead.yaml 文件中增加站点
      Homestead 目录中执行 vagrant provision
      会破坏以后数据库
      
    - 方式二 Homestead环境中的 serve 命令
      
      SSH 进入 Homestead 环境中
      执行下列命令serve domain.app /home/vagrant/Code/path/to/public/directory 80