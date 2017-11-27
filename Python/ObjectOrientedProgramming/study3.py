# coding=utf-8

# 判断类型
print type(123)   # 输出type 'int'
print type('123') # 输出type 'str'
print type(None)  # 输出type 'NoneType'

# Python把每种type类型都定义好了常量，放在types模块里，使用之前，需要先导入
import types
print type(123) == types.IntType
print type('123') == types.StringType
print type(u'abc') == types.UnicodeType
print type([]) == types.ListType
print type(str) == types.TypeType
# 最后注意到有一种类型就叫TypeType，所有类型本身的类型就是TypeType
type(int) == type(str) == types.TypeType

# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
# object -> Animal -> Dog
class Animal(object):
	def run(self):
		print 'animal is running'

class Dog(Animal):
	def run(self):
		print 'dog is running'
class Cat(Animal):
	def run(self):
		print 'cat is running'
a = Dog()           # a是Dog类的实例
b = Animal()        # b是Animal类的实例

print isinstance(a, Dog) # True        
print isinstance(a, Cat) # False
print isinstance(a, Animal) # True


# 能用type()判断的基本类型也可以用isinstance()判断：
print isinstance('123', str)
print isinstance(123, int)

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print dir('Animal')  
# 输出['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
# 主要是用来判断对象中是否含有自己想要的属性和方法
animal = Animal()  # 通过实例化一个类获得一个对象
print hasattr(animal, 'name') # 有属性'name' 输出True

print hasattr(animal, 'age') # 有属性'age'吗？输出False
setattr(animal, 'age', 19)   # 设置一个属性'age'
print hasattr(animal, 'age') # 有属性'age'吗？输出True
print getattr(animal, 'age') # 获取属性'age' 输出19
# 如果试图获取不存在的属性，会抛出AttributeError的错误：所有可以设置一个默认值
print getattr(animal, 'address', 404) # 获取属性'address'，如果不存在，返回默认值404


























