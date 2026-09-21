import os

脚本目录 = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(脚本目录, "text.txt"), encoding="utf-8") as f:
    全文 = f.read()

# 自定义: 把文档先按空行(段落)拆, 作为基本块
段落们 = [p.strip() for p in 全文.split("\n\n") if p.strip()]

# 再定义规则: 把太长的段落(>200字)再硬切一刀
结果 = []
for 段 in 段落们:
    if len(段) <= 200:
        结果.append(段)
    else:
        for i in range(0, len(段), 200):
            结果.append(段[i:i+200])

print(f"文档共{len(段落们)}个段落, 按自定义规则切成{len(结果)}块")
for i,块 in enumerate(结果[:5]):
    print(f" 块{i}: {块[:40]}...")