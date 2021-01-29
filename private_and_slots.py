# NOTE: 限制访问实例属性
# 外部代码可以自由地修改一个实例的属性，私有化变量以解决这一问题
# 私有化方法为把属性写成__属性（双下划线+属性）
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender


# 测试:
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('测试失败!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('测试失败!')
#     else:
#         print('测试成功!')


# NOTE：然而，我们可以在外部绑定新的属性，可以用slots限制外部添加属性
# 在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性

class Student_slots(object):
    __slots__ = ('name', 'gender', 'age')

    def __init__(self, name, gender, *args):
        self.__name = name
        self.__gender = gender
        self.__args = 

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

wenjie = Student_slots('wenjie', 'male')

