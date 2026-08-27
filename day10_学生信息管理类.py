class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, name, age, major):
        self.students[name] = {"age": age, "major": major}

    def find_student(self, name):
        if name in self.students:
            print(self.students[name])
        else:
            print("未找到")

    def remove_student(self, name):
        if name in self.students:
            del self.students[name]
        else:
            print("未找到")

    def show_all(self):
        print(self.students)

    def count_major(self, major):
        count = 0
        for name in self.students:
            if self.students[name]["major"] == major:
                count += 1
        return count

sm = StudentManager()
sm.add_student("张三", 20, "机械")
sm.add_student("李四", 21, "计算机")
sm.add_student("王五", 19, "机械")
sm.show_all()
sm.find_student("李四")
sm.find_student("赵六")
print(sm.count_major("机械"))
sm.remove_student("张三")
sm.show_all()
