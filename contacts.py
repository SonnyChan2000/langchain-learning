# ==== 通讯录管理 ====
contacts = {}
while True:
    print("1. 添加联系人  2.查询联系人  3.修改电话  4.删除联系人  5.显示所有联系人  6.退出")
    choice = input("请选择：")

    if choice == "1":
        name = input("请输入联系人的姓名：")
        contact = {"电话": input("请输入联系人的电话: "), "邮箱": input("请输入联系人的邮箱：")}
        contacts[name] = contact
    elif choice == "2":
        name = input("请输入需要查询的联系人姓名：")
        contact = contacts.get(name)
        if contact:
            print(f"姓名：{name}  电话：{contact['电话']}  邮箱：{contact['邮箱']}")
        else:
            print("通讯录中无该联系人")
    elif choice == "3":
        name = input("请输入需要修改电话的联系人姓名：")
        if name in contacts:
            contacts[name]["电话"] = input("请输入修改后的电话号码:")
        else:
            print("该联系人不在通讯录中")
    elif choice == "4":
        name = input("请输入需要删除的联系人姓名：")
        if name in contacts:
            del contacts[name]
        else:
            print("该联系人不在通讯录中")
    elif choice == "5":
        for name,contact in contacts.items():
            print(f"姓名：{name}  电话：{contact["电话"]}  邮箱：{contact["邮箱"]}")
    elif choice != "6":
        print("输入错误, 请重新输入")
    else:
        print("再见")
        break
    

