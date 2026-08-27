class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name}发出声音")

    def info(self):
        print(f"{self.name}今年{self.age}岁")

class Dog(Animal):
    def speak(self):
        print(f"{self.name}汪汪叫")
    def fetch(self):
        print(f"{self.name}在接飞盘")

class Cat(Animal):
    def speak(self):
        print(f"{self.name}喵喵叫")
    def climb(self):
        print(f"{self.name}在爬树")

class Bird(Animal):
    def speak(self):
        print(f"{self.name}在唱歌")
    def __init__(self, name, age, can_fly):
        super().__init__(name, age)
        self.can_fly = can_fly
    def fly(self):
        if self.can_fly:
            print(f"{self.name}在飞翔")
        else:
            print(f"{self.name}不会飞")

d = Dog("旺财", 3)
c = Cat("咪咪", 2)
b = Bird("波利", 1, True)

d.speak()
d.info()
d.fetch()
c.speak()
c.climb()
b.speak()
b.fly()
