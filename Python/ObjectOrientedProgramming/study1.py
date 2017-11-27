# coding=utf-8
# 类的概念和数据封装
class Student(object):
	def __init__(self, name, score):        # 类里面特殊的构造函数,类在实例化的时候自动调用
		self.name = name
		self.score = score

	def show(self):
		print "%s : %d" %(self.name, self.score)

s = Student('paul', 100)       # 实例化一个类
print s.name
print s.score
s.show()

# 访问限制
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改

class NewStudent(object):
	def __init__(self, name, score):        # 类里面特殊的构造函数,类在实例化的时候自动调用
		self.__name = name
		self.__score = score

	def show(self):
		print "%s : %d" %(self.__name, self.__score)
	# 获取成员变量
	def getName(self):
		return self.__name
	def getScore(self):
		return self.__score
	def setName(self, name):
		self.__name = name
	def setScore(self, score):
		self.__score = score

s = NewStudent('paul', 100)       # 实例化一个类
print s.getName()
print s.getScore()
s.show() 
s.setName('windy')
s.setScore(100)
print s.getName()
print s.getScore()
s.show() 

# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name
# 所以，仍然可以通过_Student__name来访问__name变量：
print s._NewStudent__name 
# 但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。

# 总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。








