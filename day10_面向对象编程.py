# 定义类
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name}在汪汪叫")

# 创建对象
my_dog = Dog("旺财", 3)
your_dog = Dog("小白", 1)

my_dog.bark()
your_dog.bark()

# init初始化方法
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

s1 = Student("张三", 85)
s2 = Student("李四", 92)

print(s1.name)
print(s2.score)

# 实例方法
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def introduce(self):
        print(f"我叫{self.name}, 考了{self.score}分")

    def is_pass(self):
        return self.score >= 60

s1 = Student("张三", 85)
s1.introduce()
print(s1.is_pass())

# 属性的读取与修改
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def update_score(self, new_score):
        if 0 <= new_score <= 100:
            self.score = new_score
            print(f"成绩已更新为{new_score}")
        else:
            print("分数必须在0-100之间")
s1 = Student("张三", 85)

print(s1.name)

s1.score = 95
print(s1.score)

# 直接修改属性有风险，通过方法来改，加一层校验


s1 = Student("张三", 85)
s1.update_score(150)
s1.update_score(95)
print(s1.score)

# 用类实现成绩管理
class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, name,score):
        self.students[name] = score
        print(f"已添加: {name}{score}分")

    def remove_student(self, name):
        if name in self.students:
            del self.students[name]
            print(f"已删除：{name}")

    def show_all(self):
        for name,score in sorted(self.students.items(), key=lambda x: x[1], reverse=True):
            print(f"{name}: {score}分")

    def get_average(self):
        if len(self.students) == 0:
            return 0
        return sum(self.students.values()) / len(self.students)
        

m1 = StudentManager()
m2 = StudentManager()
m1.show_all()
m1.add_student("张三", 74)
m1.add_student("李四", 87)
m2.add_student("王五", 99)
m1.show_all()
m1.remove_student("王五")
m1.get_average()
m1.remove_student("李四")
print(m1.get_average())


