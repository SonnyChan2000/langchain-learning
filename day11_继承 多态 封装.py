# 继承
class Animal:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def eat(self):
        print(f"{self.name}在吃东西")

# Dog继承Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name}在汪汪叫")

d = Dog("旺财", 3)
d.eat()
d.bark()

# 方法重写
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name}发出声音")

class Dog(Animal):
    def speak(self):
        print(f"{self.name}在汪汪叫")

class Cat(Animal):
    def speak(self):
        print(f"{self.name}在喵喵叫")

d = Dog("旺财", 3)
d.speak()

c = Cat("咪咪", 2)
c.speak()

# 多态 不同对象调用同一方法
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name}汪汪叫" 

class Cat(Animal):
    def speak(self):
        return f"{self.name}喵喵叫"

class Duck(Animal):
    def speak(self):
        return f"{self.name}嘎嘎叫"

def make_sound(animal):
    print(animal.speak())

make_sound(Dog("旺财"))
make_sound(Cat("咪咪"))
make_sound(Duck("唐老鸭"))     

# super() 省略父类中已经给过赋值方法的赋值操作
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

d = Dog("旺财", 3, "金毛")
print(d.age)
print(d.name)
print(d.breed)    

# super()追加方法
class Animal:
    def speak(self):
        print("动物发出声音", end="")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("——汪汪叫")

d = Dog()
d.speak()

# 封装
class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount >= 0:
            self.__balance += amount
            print(f"存入{amount}元, 余额{self.__balance}元")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("余额不足")
        else:
            self.__balance -= amount
            print(f"取出{amount}元, 余额{self.__balance}元")

    def show_banlance(self):
        print(f"户主{self.owner}, 余额{self.__balance}元")

account = BankAccount("张三", 1000)
#print(account.__balance) 
account.deposit(500)    
account.withdraw(2000)
account.show_banlance()

# 类属性和实例属性 写在类里面 方法外面 所有对象共用
class Student:
    school = "清华大学"

    def __init__(self, name):
        self.name = name

s1 = Student("张三")
s2 = Student("李四")

print(s1.school)
print(s2.school)
print(Student.school)

Student.school = "北京大学"    
print(s1.school)
print(s2.school)


