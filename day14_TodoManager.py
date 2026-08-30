import json
import os

class TodoManager:
    def __init__(self, filename = "tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load()
    
    def save(self):
        """把任务列表保存到JSON文件"""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent = 2)

    def load(self):
        """从JSON文件加载任务列表"""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                self.tasks = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []

    def add_task(self):
        """添加一个新任务"""
        title = input("请输入任务内容: ").strip()
        if not title:
            print("任务内容不能为空！")
            return

        priority = input("请输入优先级(高/中/低): ").strip()
        if priority not in ["高", "中", "低"]:
            priority = "中"
        task = {
            "title": title,
            "priority": priority,
            "done": False
        }
        self.tasks.append(task)
        self.save()
        print(f"已添加任务: {title}")

    def show_tasks(self):
        """显示所有任务"""
        if not self.tasks:
            print("暂无任务!")
            return
        print("\n" + "="*40)
        for i, task in enumerate(self.tasks):
            status = "√" if task["done"] else "o"
            print(f"{i+1}.[{status}][{task['priority']}]{task['title']}")
            print("=" * 40 + "\n")

    def complete_task(self):
        """标记任务为已完成"""
        self.show_tasks()
        if not self.tasks:
            return

        try:
            idx = int(input("请输入要完成的任务编号: ")) - 1
            if 0 <= idx < len(self.tasks):
                self.tasks[idx]["done"] = True
                self.save()
                print(f"已完成: {self.tasks[idx]['title']}")
            else:
                print("编号超出范围!")
        except ValueError:
            print("请输入有效的数字编号!")

    def delete_task(self):
        """删除一个任务"""
        self.show_tasks()
        if not self.tasks:
            return

        try:
            idx = int(input("请输入要删除的任务编号: ")) - 1
            if 0 <= idx < len(self.tasks):
                removed = self.tasks.pop(idx)
                self.save()
                print(f"已删除: {removed['title']}")
            else:
                print("编号超出范围!")
        except ValueError:
            print("请输入有效的数字编号!")

    def sort_by_priority(self):
        """按优先级排序(高-中-低)"""
        priority_order = {"高": 0, "中": 1, "低": 2}
        self.tasks.sort(key= lambda t: priority_order.get(t["priority"], 1))
        self.save()
        print("已按优先级排序!")
        self.show_tasks()

    def run(self):
        """运行主程序"""
        while True:
            print("\n" + "="*10 + "待办事项管理器" + "="*10)
            print("1.添加任务")
            print("2.完成任务")
            print("3.删除任务")
            print("4.查看所有任务")
            print("5.按优先级排序")
            print("6.退出")
            print("="*27)
            choice = input("请选择操作: ").strip()
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.complete_task()
            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                self.show_tasks()
            elif choice == "5":
                self.sort_by_priority()
            elif choice == "6":
                print("再见!")
                break
            else:
                print("无效选择, 请输入1-6")
if __name__ == "__main__":
    app = TodoManager()
    app.run()


