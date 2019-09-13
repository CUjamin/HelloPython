from functools import reduce
import math

# print("HelloPython")

# -------------------------------------map()-------------------------------------
# def format_name(s):
#     return s[0].upper() + s[1:].lower()
#
# for s in map(format_name, ['adam', 'LISA', 'barT']):
#     print(s)
#
# print(map(format_name, ['adam', 'LISA', 'barT']))
#
# # reduce()
# def prod(x, y):
#     return x*y
#
# print(reduce(prod, [2, 4, 5, 7, 12]))

# -------------------------------------filter()-------------------------------------
#
# def is_sqr(x):
#     r = int(math.sqrt(x))
#     if x==r*r:
#         return x
#
# for s in filter(is_sqr, range(1, 101)):
#     print(s)
# print(filter(is_sqr, range(1, 101)))

# -------------------------------------sorted()---------------------------------------
# def cmp_ignore_case(s1, s2):
#     c1 = s1.upper()
#     c2 = s2.upper()
#     if(c1<c2):return 1
#     elif(c1>c2):return -1
#     else:return 0
#
# for s in sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case):
#     print(s)
#
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case))
#--------------------------------------python中返回函数------------------------------------
# def calc_prod(lst):
#     def f(lst):
#         s = 1
#         for temp in lst:
#             s*=temp
#         return s
#     return f(lst)
#
# f = calc_prod([1, 2, 3, 4])
# print(f)
#--------------------------------------python中闭包-----------------------------------------
#像这种内层函数引用了外层函数的变量（参数也算变量），然后返回内层函数的情况，称为闭包（Closure）。
#闭包的特点是返回的函数还引用了外层函数的局部变量，所以，要正确使用闭包，就要确保引用的局部变量在函数返回后不能变。
# def count():
#     fs = []
#     for i in range(1, 4):
#         ???
#         fs.append(???)
#     return fs
#
# f1, f2, f3 = count()
# print(f1(), f2(), f3())
#
# fs中存了三个方法，这三个方法均使用外部变量i，因为count()执行时，结果会由当前外部变量i的值决定;
# 当f1, f2, f3执行时，方法中的i均已变成了3
# def count():
#     fs = []
#     for i in range(1, 4):
#         def f():
#              return i*i
#         print('f=%s,i*i=%s'%(f,i*i))
#         fs.append(f)
#     return fs
#
# f1, f2, f3 = count()
# print('f1=%s,f2=%s,f3=%s'%(f1(), f2(), f3()))

#它可以正确地返回一个闭包g，g所引用的变量j不是循环变量，因此将正常执行。
# 在count函数的循环内部，如果借助f函数，就可以避免引用循环变量i。
# def count():
#     fs = []
#     for i in range(1, 4):
#         #f(j)函数返回一个方法g，g所引用的变量j不是循环变量
#         def f(j):
#             def g():
#                 return j*j
#             return g
#         r = f(i)
#         fs.append(r)
#     return fs
#
# f1, f2, f3 = count()
# print(f1(), f2(), f3())

# -----------------------------python中匿名函数----------------------------------------
# def is_not_empty(s):
#     return s and len(s.strip()) > 0
#
# print(filter(lambda  s: s and len(s.strip()) > 0,['test', None, '', 'str', '  ', 'END'] ))
#
# for x in filter(lambda  s: s and len(s.strip()) > 0,['test', None, '', 'str', '  ', 'END'] ):
#     print(x)

# ------------------------------装饰器--------------------------------------------------
# Python的 decorator 本质上就是一个高阶函数，
# 它接收一个函数作为参数，然后，返回一个新函数。
# def new_fn(f):
#     def fn(x):
#         print('call '+f.__name__+'()')
#         return f(x)
#     return fn
#
# # f1 = new_fn(f1)
# # print(f1(5))
# @new_fn
# def f1(x):
#     return x*2
# @new_fn
# def f2(x):
#     return x*10
# @new_fn
# def f3(x):
#     return x*x
#
# print(f1(5),f2(5),f3(5))

# def log(f):
#     def fn(*args,**kw):
#         print('call ' + f.__name__ + '()...')
#         return f(*args,**kw)
#     return fn
#
# @log
# def factorial(n):
#     return reduce(lambda x,y: x*y, range(1, n+1))
# print(factorial(10))
#
# @log
# def add(x, y):
#     return x + y
# print(add(1, 2))
# -------------------------任务-------------------
# 请编写一个@performance，它可以打印出函数调用的时间。
# import time
#
# def performance(f):
#     def fn(*args, **kw):
#         t1 = time.time()
#         r = f(*args, **kw)
#         t2 = time.time()
#         print('call %s() in %fs' % (f.__name__, (t2 - t1)))
#         return r
#     return fn
#
# @performance
# def factorial(n):
#     return reduce(lambda x,y: x*y, range(1, n+1))
#
# print(factorial(10))

# ----------------------python中编写带参数decorator-------------------
# @performace增加一个参数，允许传入's'或'ms'：
# import time
#
# def performance(unit):
#     def r0(f):
#         def fn(*args, **kw):
#             t1 = time.time()
#             r = f(*args, **kw)
#             t2 = time.time()
#             if unit=='ms':
#                 u=1000
#             elif unit=='s':
#                 u=1
#             print('call %s() in %f %s' % (f.__name__, (t2 - t1)*u,unit))
#             return r
#         return fn
#     return r0
#
# @performance('ms')
# def factorial(n):
#     return reduce(lambda x,y: x*y, range(1, n+1))
#
# print(factorial(10))
# ----------------------------python中完善decorator----------------------------
# import time, functools
#
# def performance(unit):
#     def r0(f):
#         @functools.wraps(f)
#         def fn(*args, **kw):
#             t1 = time.time()
#             r = f(*args, **kw)
#             t2 = time.time()
#             if unit=='ms':
#                 u=1000
#             elif unit=='s':
#                 u=1
#             print('call %s() in %f %s' % (f.__name__, (t2 - t1)*u,unit))
#             return r
#         return fn
#     return r0
#
# @performance('ms')
# def factorial(n):
#     return reduce(lambda x,y: x*y, range(1, n+1))
#
# print(factorial.__name__)
# ------------------------------------python中偏函数-----------------------------
# functools.partial可以把一个参数多的函数变成一个参数少的新函数，
# 少的参数需要在创建时指定默认值，这样，新函数调用的难度就降低了。

# import functools
# sorted_ignore_case = functools.partial(sorted, key = str.lower)
# print(sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit']))

#--------------------------------------python中动态导入模块------------------------
#
# try:
#     import json
# except ImportError:
#     import simplejson as json
#
# print(json.dumps({'python':3.6}))

# ------------------------------------python之使用__future__ --------------------------
# from __future__ import unicode_literals

# s = 'am I an unicode?'
# print(isinstance(s,str))

# --------------------------------------面向对象---------------------------------------
# class Person(object):
#     pass
# xiaoming = Person()
# xiaohong = Person()
#
# print(xiaohong)
# print(xiaohong)
# print(xiaoming)
# -------------------------------------python中创建实例属性-----------------------------
# class Person(object):
#     pass
#
# p1 = Person()
# p1.name = 'Bart'
#
# p2 = Person()
# p2.name = 'Adam'
#
# p3 = Person()
# p3.name = 'Lisa'
#
# L1 = [p1, p2, p3]
# L2 = [p2, p1, p3]
#
# print(L2[0].name)
# print(L2[1].name)
# print(L2[2].name)

# ------------------------------------python中初始化实例属性------------------------------
# class Person(object):
#     def __init__(self,name,sex,birthday,job):
#         self.name = name
#         self.sex = sex
#         self.birthday = birthday
#         self.job =  job
#
# xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')
#
# print(xiaoming.name)
# print(xiaoming.job)
#
# class Person(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.__score = score
#
# p = Person('Bob', 59)
#
# print(p.name)
# try:
#     print(p.__score)
# except AttributeError:
#     print ('attributeError')
# -----------------------------------------python中创建类属性---------------------------------
# class Person(object):
#     count = 0
#     def __init__(self, name):
#         Person.count += 1
#         self.name = name
#
#
# p1 = Person('Bob')
# print(Person.count)
#
# p2 = Person('Alice')
# print(Person.count)
#
# p3 = Person('Tim')
# print(Person.count)
# -------------------------------------python中类属性和实例属性名字冲突怎么办-------------------
# class Person(object):
#     __count = 0
#
#     def __init__(self, name):
#         Person.__count = Person.__count + 1
#         self.name = name
#         print(Person.__count)
#
#     def get__count(self):
#         return self.__cont
#
#
# p1 = Person('Bob')
# p2 = Person('Alice')
#
# print(Person.get__count())
# ----------------------------------------python中定义实例方法-------------------------------
# class Person(object):
#     __score = 0
#     def __init__(self, name, score):
#         self.name = name
#         self.__score = score
#
#     def get_grade(self):
#         if self.__score>=90:
#             level = 'A'
#         elif self.__score>=60:
#             level = 'B'
#         else:
#             level = 'C'
#         return level
#
# p1 = Person('Bob', 90)
# p2 = Person('Alice', 65)
# p3 = Person('Tim', 48)
#
# print(p1.get_grade())
# print(p2.get_grade())
# print(p3.get_grade())

# ----------------------------python中方法也是属性------------------------------
# class Person(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#         self.get_grade = lambda: 'A'
#
# p1 = Person('Bob', 90)
# print(p1.get_grade)
# print(p1.get_grade())
# ---------------------------python中定义类方法--------------------------------
# class Person(object):
#
#     __count = 0
#     def __init__(self,name):
#         self.name = name
#         Person.__count+=1
#
#     @classmethod
#     def how_many(cls):
#         return cls.__count
#
# print(Person.how_many())
#
# p1 = Person('Bob')
#
# print(Person.how_many())
# # ----------------------------python 继承关系------------------------------------------
# class Person(object):
#     def __init__(self,name,gender):
#         self.name = name
#         self.gender = gender
#
# class Student(Person):
#     def __init__(self,name,gender,school,score):
#         super(Student,self).__init__(name,gender)
#         self.school = school
#         self.score = score
# # ----------------------------python 组合关系------------------------------------------
# class Book(object):
#     def __init__(self,name):
#         self.name = name
#
# class Student(Person):
#     def __init__(self,name,gender,school,score,bookName):
#         super(Student,self).__init__(name,gender)
#         self.school = school
#         self.score = score
#         self.book = Book(bookName)

# ----------------------------python中继承一个类-----------------------------------------
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Teacher(Person):

    def __init__(self, name, gender, course):
        super(Teacher,self).__init__(name,gender)
        self.course = course

t = Teacher('Alice', 'Female', 'English')
print(t.name)
print(t.course)
