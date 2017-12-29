# coding=utf-8

# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。

colors = ['red', 'green', 'blue', 'purple', 'orange', 'pink']
print colors[3]   # 输出purple
print colors     # 输出['red', 'green', 'blue', 'purple', 'orange', 'pink']
print len(colors)      # 输出6

# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
print colors[-1]
# 以此类推，可以获取倒数第2个、倒数第3个：

# 追加元素到list末尾
colors.append('silver ')
print colors  # 输出['red', 'green', 'blue', 'purple', 'orange', 'pink', 'silver ']

# 也可以把元素插入到指定的位置，比如索引号为1的位置：
colors.insert(1, 'black ')
print colors  # 输出['red', 'black ', 'green', 'blue', 'purple', 'orange', 'pink', 'silver ']

# 删除list末尾的元素
colors.pop()
print colors

# 删除指定位置的元素,参数为对应的索引
colors.pop(1)
print colors

# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates = ('Bob', 'John', 'Tony', 'Danna', 'Windy', 'Gary')
# 现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。

# 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
# 如果要定义一个空的tuple，可以写成()：
t = ()
print t

# 但是，要定义一个只有1个元素的tuple，不能定义成t = ('abc'), 会和数学公式中的小括号，这就产生了歧义，被解析成 t = 'abc', 应该定义成
t= ('abc',)
print t

# tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
# 所有 tople 中有元素是list， list中有元素可以改变是正常的,但不能改变list指向
l = ['A', 'B']
t = ('a', 'b', l)
print t
# l = [1, 2] 不能这样
# 可以这样
l[0] = 1
l[1] = 2
print t

# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
# 如果用dict实现，只需要一个“名字”-“成绩”的对照表，直接根据名字查找成绩，无论这个表有多大，查找速度都不会变慢。用Python写一个dict如下：
d = {'Bob' : 95, 'John' : 88, 'Tony' : 92, 'Danna' : 98, 'Windy' : 100, 'Gary' : 94}
print d['Gary'] #这种取法在键不存在时会报错,可以用dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value用
print d.get('Danna')

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 要创建一个set，需要提供一个list作为输入集合：
s = set([1, 2, 3])
print s
# 注意，传入的参数[1, 2, 3]是一个list，而显示的set([1, 2, 3])只是告诉你这个set内部有1，2，3这3个元素，显示的[]不表示这是一个list。
# 重复元素在set中自动被过滤：
s = set([1, 2, 1, 3, 2, 4, 5, 6, 3])
print s

#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s. add (7)
s. add (7)
s. add (8)
print s

# 通过remove(key)方法可以删除元素：
s.remove(7)
s.remove(8)
print s

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([1, 2 , 4, 5, 6])
print s1 & s2   # 输出set([1, 2])
print s1 | s2   # 输出set([1, 2, 3, 4, 5, 6])


# 可变与不可变
# 对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：
l = [1, 4, 6, 3, 8, 9]
l.sort()
print l

# 而对于不可变对象，比如str，对str进行操作呢：
a = 'abc'
b = a.replace('a', 'A')
print a
print b
# 当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。相反，replace方法创建了一个新字符串'Abc'并返回，如果我们用变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了：