# coding=utf-8

# 序列化https://docs.python.org/2/library/json.html#json.dumps
# 在程序运行的过程中，所有的变量都是在内存中，比如，定义一个dict：
# d = dict(name='Bob', age=20, score=88)
# 可以随时修改变量，比如把name改成'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。
# 如果没有把修改后的'Bill'存储到磁盘上，下次重新运行程序，变量又被初始化为'Bob'。

# 我们把变量从内存中变成可存储或传输的过程称之为序列化。
# 在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。

# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

# Python提供两个模块来实现序列化：cPickle和pickle。这两个模块功能是一样的。
# 区别在于cPickle是C语言写的，速度快，pickle是纯Python写的，速度慢，跟cStringIO和StringIO一个道理。
# 用的时候，先尝试导入cPickle，如果失败，再导入pickle：


try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(name = 'Bob', age = 20, score = 88)
print pickle.dumps(d)

# pickle.dumps()方法把任意对象序列化成一个str，然后，就可以把这个str写入文件。
# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
f = open('dump.log', 'wb')
pickle.dump(d ,f)
f.close()

# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个str，然后用pickle.loads()方法反序列化出对象
f = open('dump.log', 'rb')
d = pickle.load(f)
f.close()
print d

# 当然，这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。

# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容。
# 因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。

# JSON
# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为JSON。
# 因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
# JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

# JSON类型	             Python类型
# {}	                     dict
# []	                     list
# "string"	             'str'或u'unicode'
# 1234.56	                 int或float
# true/false	             True/False
# null	                 None

# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：
import json
print json.dumps(d)
# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
f = open('dump2.log', 'wb')
json.dump(d, f)
f.close()

# 从文件中读取存入的json字符串,再把JSON反序列化为Python对象，用loads()或者对应的load()方法
f = open('dump2.log', 'rb')
d = json.load(f)
f.close()
print d # 输出{u'age': 20, u'score': 88, u'name': u'Bob'}
# 有一点需要注意，就是反序列化得到的所有字符串对象默认都是unicode而不是str。python默认把字符串转为unicode编码格式
# 由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str或unicode与JSON的字符串之间转换。

# 对象序列化
# Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：
# import json

# def json_load_byteified(file_handle):
#     return _byteify(
#         json.load(file_handle, object_hook=_byteify),
#         ignore_dicts=True
#     )

# def json_loads_byteified(json_text):
#     return _byteify(
#         json.loads(json_text, object_hook=_byteify),
#         ignore_dicts=True
#     )

# def _byteify(data, ignore_dicts = False):
#     # if this is a unicode string, return its string representation
#     if isinstance(data, unicode):
#         return data.encode('utf-8')
#     # if this is a list of values, return list of byteified values
#     if isinstance(data, list):
#         return [ _byteify(item, ignore_dicts=True) for item in data ]
#     # if this is a dictionary, return dictionary of byteified keys and values
#     # but only if we haven't already byteified it
#     if isinstance(data, dict) and not ignore_dicts:
#         return {
#             _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
#             for key, value in data.iteritems()
#         }
#     # if it's anything else, return it in its original form
#     return data
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
print(json.dumps(s, default=lambda obj: obj.__dict__))

















































