# coding=utf-8

# 使用__slots__
# 当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：
s = Student()
s.name = "Athena"
print s.name
# 定义一个函数作为实例方法
def set_age(self, age): 
	self.age = age

# 给实例绑定一个方法
from types import MethodType
s.set_age = MethodType(set_age, s, Student) 
s.set_age(25) # 调用实例方法
print s.age






























