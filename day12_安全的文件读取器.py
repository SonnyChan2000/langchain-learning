def read_file_safe(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print(f"文件不存在:{filename}")
    except (Exception) as e:
        print(f"读取文件时出错: {e}")
    finally:
        print("文件读取操作完成")

read_file_safe("test.txt")
read_file_safe("不存在.txt")
    