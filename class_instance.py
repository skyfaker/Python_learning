'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point({},{})".format(self.x, self.y)

    def show(self):
        print(self.x, self.y)


p1 = Point(3, 4)
print(p1)
print(p1.__dict__)
p1.__dict__['y'] = 10
print(p1.__dict__)
p1.z = 20
print(p1.__dict__)
print(dir(p1))
print(p1.__dir__())
'''
from types import MethodType

class Student():
    name = 'class'
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_score(self):
        print('inside')
        print(self)
        return self.score


def outside_get(self):
    print('outside')
    print(self)
    return self.name

def outside_no_self_get():
    print('no self')
    return 'a'


j = Student('jack', 90)
# print(j)
print(j.get_score())
print('-*'*20)

# NOTE：1. 这种直接绑定到实例，实际上是替换掉了原来的j.get_score，作为outside_get的一个别名，对其他实例没有影响
# j.get_score = outside_get
# # print(j.get_score()) 报错
# print(j.get_score(j)) # 需要这样调用

# k = Student('kk', 88)
# print(k.get_score()) 


# NOTE：2. MethodType绑定到实例，成为一个实例方法，自动传入实例作为self，不会影响其他实例
# j.get_score = MethodType(outside_get, j)
# print(j.get_score())

# k = Student('kk', 88)
# print(k.get_score()) 


# NOTE： 3. 动态绑定到类的实例方法，会覆盖已有的同名的实例方法,所有实例都可以继承，包括已经实例化的实例
# Student.get_score = outside_get
# print(j.get_score())

# k = Student('kk', 88)
# print(k.get_score()) 


# NOTE： 4. MethodType绑定到类相当于动态绑定到类方法，即使是实例调用，实际传入self的是class而不是实例
Student.get_score = MethodType(outside_get, Student)
print(j.get_score())

k = Student('kk', 88)
print(k.get_score()) 
