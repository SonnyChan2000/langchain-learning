class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        print(f"{self.breed}{self.name}在汪汪叫, 它{self.age}岁了")

    def human_age(self):
        return self.age * 7

d1 = Dog("旺财", 3, "金毛")
d2 = Dog("小黑", 2, "拉布拉多")
d1.bark()
print(d1.human_age())
d2.bark()
        