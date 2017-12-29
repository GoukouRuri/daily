# coding=utf-8

# if语句(注意python的缩进规范)
age = 23
if age < 12:
  print 'your age is ' + str(age)
  print 'you are child'
elif age < 18:
  print 'your age is ' + str(age)
  print 'you are teenager'
else:
  print 'your age is ' + str(age)
  print 'you are adult'


# for x in [] 语句
sum = 0
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
for x in list:
  sum += x
print sum

# 或者是
sum = 0
for x in range(0, 100):
  sum += x
print sum

# while语句(很少有用到)
sum = 0
n = 99
while n > 0:
  sum = sum + n
  n = n - 2
print sum