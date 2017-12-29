> ### For Windows System
### Jdk的安装(java虚拟机及相关jar包)

  - 安装

    - 选择第三个独立jdk,jre环境
    - 无脑安装

  - 配置环境变量

    - 配置JAVA_HOME：计算机→属性→高级系统设置→环境变量→系统变量中新建→输入变量名：JAVA_HOME,变量值：JDK安装路径；

      - 例如D:\java8\jdk1.8.0_40

    - 配置JRE_HOME:计算机→属性→高级系统设置→环境变量→系统变量中新建→输入变量名

      - 例如D:\java8\jre

    - 将新建的两个系统变量加入path变量

      - %JRE_HOME%;%JAVA_HOME%\bin;

    - 配置CLASS_PATH变量(注意最前面有一个点号，不能掉):计算机→属性→高级系统设置→环境变量→系统变量中新建→输入变量名

      - .;%JAVA_HOME%\lib;%JAVA_HOME%\jre\lib

<<< 至此,cmd中输入java -version出现正常结果表示安装成功

  - 如果不想用绝对路径就可以直接使用javac命令

    - path变量加入javac.exe路径: 例如D:\java8\jdk1.8.0_40\bin

### tomcat配置

  - 下载windows下64位zip包(一定要是zip包,解压到指定目录)

    - bin目录下startup.bat为tomcat启动脚本, shutdown.bat为停止脚本

      - 点击tomcat安装目录下的bin目录中的startup.bat，会出现一闪而过的情况，解决方案如下：编辑startup.bat，在文本最后面一行加pause，可以使运行在中断处停止；

  - 配置环境变量：同上配置JDK的环境变量一样，增加一个CATALINE_HOME，变量值为：tomcat的安装目录

    - 例如D:\tomcat9

  - 启动tomcat/bin中的startup.bat，出现成功页面，表明tomcat启动成功,有error根据error排错,一般可能是java环境变量配置出错
  - 测试tomcat是否正常启动

    - 一般默认8080端口，现阶段tomcat6后版本安装时可以指定相关配置,访问localhost:8080，出现tom猫界面,表示成功,失败请自行google，一般默认配置不会又问题

### java web项目部署

  - 在myeclipse或者spring ide等开发软件中选中你要发布的项目, 右键Export，导出war文件。将生成的war文件，复制到服务器上的tomcat webapps路径下,重启tomcat即可(war包会自动解压)
