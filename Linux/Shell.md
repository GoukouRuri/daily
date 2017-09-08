## bash shell 简单入门

> [基础教程传送门](http://www.runoob.com/w3cnote/shell-quick-start.html)

> shell是一个命令行解释器

  - #!/bin/bash        作用标识是bash shell脚本

> shell脚本的执行方式

  - 赋予执行权限后直接执行
  
    `chmod 755 test.sh
    ./test.sh
    `
  - 通过bash执行（不需要赋予文件执行权限，因为这个是用bash解释shell文件）
  
    `bash ./test.sh`

### `echo`输出命令

  - echo [选项] [输出内容]
  
    - -e: 支持反斜杠控制字符的转换
    
### `cat -A [文件名]` 可以查看到文件所有字符，包括隐藏字符（如换行符）

###  将windos下编译的文件转化为unix下编译的
     `yum -y install dos2unix`
     dos2unix [文件名]`
