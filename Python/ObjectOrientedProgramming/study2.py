# coding=utf-8

# 继承和多态

# 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass）、衍生类
# 而被继承的class称为基类、父类或超类（Base class、Super class）。

# 比如定义一个基类Animals, 有个方法run
class Animal(object):
	def run(self):
		print 'animal is running'

class Dog(Animal):
	def run(self):
		print 'dog is running'
class Cat(Animal):
	def run(self):
		print 'cat is running'
# 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。
dog = Dog()
cat = Cat()
print dog.run()
print cat.run()

# 要理解什么是多态，我们首先要对数据类型再作一点说明。
# 判断一个变量是否是某个类型可以用isinstance()判断
a = Dog()           # a是Dog类的实例
b = Animal()        # b是Animal类的实例

print isinstance(a, Dog) # True        
print isinstance(a, Cat) # False
print isinstance(a, Animal) # True

# 看来c不仅仅是Dog，c还是Animal！
# 不过仔细想想，这是有道理的，因为Dog是从Animal继承下来的，当我们创建了一个Dog的实例c时，我们认为c的数据类型是Dog没错，但c同时也是Animal也没错，Dog本来就是Animal的一种！
# 所以，在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行

# 小结

# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写；
# 有了继承，才能有多态。在调用类实例方法的时候，尽量把变量视作父类类型，这样，所有子类类型都可以正常被接收；
# 旧的方式定义Python类允许不从object类继承，但这种编程方式已经严重不推荐使用。任何时候，如果没有合适的类可以继承，就继承自object类。

























