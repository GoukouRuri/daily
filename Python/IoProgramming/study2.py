# coding=utf-8

# 如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令。

# 如果要在Python程序中执行这些目录和文件的操作怎么办？
# 其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数。

# 打开Python交互式命令行，我们来看看如何使用os模块的基本功能：

import os
print os.name  # posix

# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

# 要获取详细的系统信息，可以调用uname()函数：

print os.uname()

# 在操作系统中定义的环境变量，全部保存在os.environ这个dict中，可以直接查看：
print os.environ

# 要获取某个环境变量的值，可以调用os.getenv()函数：
print os.getenv('PATH')

# 操作文件和目录

# 查看当前目录的绝对路径:
print os.path.abspath('.')

# 在某个目录下创建一个新目录，
# 首先把新目录的完整路径表示出来:
os.path.join('/data/wwwroot/default/pystudy/pythonIO编程', 'test')

# 然后创建一个目录:
os.mkdir('/data/wwwroot/default/pystudy/pythonIO编程/test')
# 删掉一个目录:
os.rmdir('/data/wwwroot/default/pystudy/pythonIO编程/test')












