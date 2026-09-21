import os
from langchain_text_splitters import(
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter,
)

脚本目录 = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(脚本目录, "text.txt"), encoding="utf-8") as f:
    全文 = f.read()

print(f"原始长度: {len(全文)}字符\n")

# 1) CharacterTextSplitter: 固定100字硬切
a = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
块a = a.split_text(全文)
print(f"[CharacterTextSplitter]切成{len(块a)}块")
print(f"第1块: {块a[0][:60]}...")
print(f"最后一块: {块a[-1][:60]}...\n")
print(f"每块长度: {[len(x) for x in 块a][:10]}...")   # 打印前几块的实际字符数


# 2) RecursiveCharacterTextSplitter: 递归聪明切
b = RecursiveCharacterTextSplitter(separators=["\n\n","\n","，","。"," ",""],
                                   chunk_size=100, chunk_overlap=0)
块b = b.split_text(全文)
print(f"[RecursiveCharacterTextSplitter]切成{len(块b)}块")
print(f" 第1块: {块b[0][:60]}...")
print(f" 最后一块: {块b[-1][:60]}...")

a2 = CharacterTextSplitter(separator="\n", chunk_size=100, chunk_overlap=0)
块a2 = a2.split_text(全文)
print(f"[CharacterTextSplitter] 切成 {len(块a2)} 块")
print(f"各块长度: {[len(x) for x in 块a2]}")