import os
from langchain_text_splitters import RecursiveCharacterTextSplitter

脚本目录 = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(脚本目录, "text.txt"), encoding="utf-8") as f:
    全文 = f.read()

for 尺寸 in [50, 200, 800]:
    切 = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n","，","。"," ",""],
        chunk_size = 尺寸,
        chunk_overlap=0,
    )
    块们 = 切.split_text(全文)
    print(f"chunk_size={尺寸} → 切成{len(块们)}块")
    print(f" 第1块: {块们[0][:40]}...\n")