# coding=utf-8

# 字符串编码

# 字符串和asci码之间的转化
ord('A')  # 将字母转化为asci码
chr(65)   # 将asci码转化为字母等

# 对Unicode的支持,以Unicode表示的字符串用u'...'表示
print u'你好'
# Unicode格式转为utf-8格式,需要用encode('utf-8')
print u'ABC'. encode('utf-8')

# len()返回字符串长度
print len('hello world') # 输出11

# 如何输出格式化的字符串
# 最后一个常见的问题是如何输出格式化的字符串。
# 我们经常会输出类似'亲爱的xxx你好！你xx月的话费是xx，余额是xx'之类的字符串，而xxx的内容都是根据变量变化的，
# 所以，需要一种简便的格式化字符串的方式
data = 'name %s, age %d'
data = data % ('GoukouRuri', 23)
print data