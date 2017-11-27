# coding=utf-8

# 安装第三方模块

# 在Python中，安装第三方模块，是通过setuptools这个工具完成的。Python有两个封装了setuptools的包管理工具：easy_install和pip。目前官方推荐使用pip。
# 如果你正在使用Mac或Linux，安装pip本身这个步骤就可以跳过了。
# 如果你正在使用Windows，请参考安装Python一节的内容，确保安装时勾选了pip和Add python.exe to Path。
# 在命令提示符窗口下尝试运行pip，如果Windows提示未找到命令，可以重新运行安装程序添加pip。
# 现在，让我们来安装一个第三方库——Python Imaging Library，这是Python下非常强大的处理图像的工具库。
# 一般来说，第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索
# 比如Python Imaging Library的名称叫PIL，因此，安装Python Imaging Library的命令就是：

# pip install PIL
# 或者pip install pillow

from PIL import Image
im = Image.open('test.png')
print im.format, im.size, im.mode

im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')

# 模块搜索路径
# 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：
import sys
print sys.path


# 如果我们要添加自己的搜索目录，有两种方法：
# 第一种方法是直接修改sys.path，添加要搜索的目录：
# import sys

# sys.path.append('/Users/michael/my_py_scripts')

# 第二种方法是设置环境变量PYTHONPATH















