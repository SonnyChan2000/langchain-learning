---
AIGC:
    Label: "1"
    ContentProducer: 001191110102MACQD9K64018705
    ProduceID: 2578808644311235_0/project_7671958131122929930-files/学习计划/Day25_知识库资料_AI学习笔记.md
    ReservedCode1: ""
    ContentPropagator: 001191110102MACQD9K64028705
    PropagateID: 2578808644311235#1788933698058
    ReservedCode2: ""
---
# Sonny 的 AI Agent 开发学习笔记

> 本文件是个人学习资料，用于上传到扣子（Coze）知识库，供「个人知识助手」检索回答。
> 内容覆盖 2026 年 9 月学习计划第 15-24 天的核心知识点。

---

## 一、学习计划概览

- 总计划：14 周从零转型 AI Agent 开发工程师，目标 2026 年 11 月中旬在杭州投递简历。
- 学习者背景：机械专业，2 年机械工作经验，零基础自学编程。
- 代码练习目录：本地 `D:\python_learning`，使用 Git 管理，API 密钥存放在 `.env` 文件中并通过 `.gitignore` 排除，不提交到仓库。
- 使用的大模型平台：阿里百炼（DashScope），通过 OpenAI 兼容模式调用，base_url 为 `https://dashscope.aliyuncs.com/compatible-mode/v1`。
- 使用的模型：对话用 qwen-turbo，文本向量化用 text-embedding-v4。

## 二、大模型 API 调用基础

- 使用 OpenAI SDK 调用大模型，核心接口是 `client.chat.completions.create()`。
- 消息用列表传递，每条消息有 role 和 content 两个字段。
- role 有三种：system（设定 AI 的身份和规则）、user（用户提问）、assistant（AI 的回复）。
- API Key 通过环境变量读取，代码里用 `os.getenv("DASHSCOPE_API_KEY")`，严禁把密钥硬编码在代码里。
- 回复内容在 `response.choices[0].message.content` 里。

## 三、Prompt Engineering（提示词工程）

- System Prompt 是控制大模型行为最有效的手段，写在 system 角色消息里。
- 好的提示词结构：角色定位 + 任务说明 + 输出格式要求 + 限制条件。
- 带换行的长提示词用 Python 三引号字符串编写，f-string 三引号不要漏掉 f 前缀。
- 提示词里可以用「示例」（few-shot）给模型示范期望的输出格式。

## 四、Temperature（温度参数）

- temperature 控制模型输出的随机性，取值范围 0 到 2。
- temperature 越低（如 0），输出越稳定、确定，适合事实问答、代码生成。
- temperature 越高（如 1.5），输出越发散、有创意，适合写诗、头脑风暴。

## 五、Function Calling（函数调用）

- Function Calling 让大模型不只会说话，还能调用外部工具。
- 流程：用户提问 → 模型判断需要调工具 → 返回要调用的函数名和参数 → 程序执行函数 → 把结果回传给模型 → 模型生成最终回答。
- 函数定义要以 JSON Schema 格式描述：name（函数名）、description（函数用途，模型靠它判断何时调用）、parameters（参数说明）。
- description 写得越清楚，模型越知道什么时候该用这个工具。

## 六、ReAct 模式

- ReAct = Reasoning（推理）+ Acting（行动），是 Agent 的核心决策循环。
- 循环过程：Thought（思考该干什么）→ Action（调用工具）→ Observation（观察结果）→ 再 Thought，直到能回答用户。
- ReAct 让 Agent 可以多步解决问题，而不是一问一答。

## 七、Embedding（文本向量化）

- Embedding 把文本转换成一串数字（向量），语义相近的文本向量距离也近。
- 调用接口：`client.embeddings.create(model="text-embedding-v4", input=文本)`，结果在 `resp.data[0].embedding`。
- 余弦相似度（cosine similarity）衡量两个向量的方向接近程度，取值范围 -1 到 1：1 表示完全相同，0 表示无关，-1 表示相反。
- 实测案例：「我今天很开心」和「我今天心情很好」相似度 0.8872；「我今天很开心」和「今天下雨了」相似度 0.5258。

## 八、语义检索（TopK）

- 语义检索流程：把知识库所有文档向量化存好 → 用户提问向量化 → 计算问题向量和每个文档向量的余弦相似度 → 按分数从高到低排序 → 取最相关的前 K 条（TopK）。
- 关键词检索靠字面匹配，搜「AI智能体开发」匹配不到只写了「LangChain」的文档；语义检索能理解含义，可以匹配到。

## 九、RAG（检索增强生成）完整流程

- RAG = Retrieval-Augmented Generation，检索增强生成。
- 完整流程：①文档切分（chunking，按空行或固定长度切成片段）②向量化建库（embedding）③检索（用户问题向量化，算相似度，取 TopK）④拼装提示词（把检索到的资料塞进 prompt）⑤生成（大模型基于资料回答）。
- 文档切分用 `split("\n\n")` 按空行切分，列表推导式 `[sec.strip() for sec in raw.split("\n\n") if sec.strip()]` 可以同时去掉空白片段。
- RAG 的价值：解决大模型知识过时、不知道私有资料、容易幻觉的问题。
- 系统提示词里必须要求模型「只根据提供的资料回答，资料里没有就说不知道」，否则模型会编造。

## 十、RAG 和 Agent 的本质区别

- RAG 像被动的图书管理员：你问，它查资料，照着资料回答，不会主动做别的事。
- Agent 像主动办事的助理：有 ReAct 决策循环，能自己判断该做什么、调用什么工具、分多步完成任务。
- RAG 是 Agent 常用的一个技能（查资料），但 Agent 的能力边界远大于 RAG。

## 十一、FastAPI 服务化

- FastAPI 是 Python 的 Web 框架，用来把大模型能力包装成 HTTP 接口对外提供服务。
- 安装命令：`pip install fastapi "uvicorn[standard]"`。
- 启动命令：`uvicorn 文件名:app --port 端口号`，注意文件名和 app 之间是**冒号**不是点号，例如 `uvicorn day24_hello:app --port 8010`。
- 代码里必须有 `from fastapi import FastAPI` 和 `app = FastAPI()`，否则启动时报 `Attribute "app" not found`。
- 定义 GET 接口用 `@app.get("/路径")`，路径参数用 `@app.get("/hello/{name}")`。
- 定义 POST 接口用 `@app.post("/路径")`，请求体用 Pydantic 模型类接收。
- 启动后浏览器打开 `http://127.0.0.1:8000/docs` 是 Swagger UI 在线接口测试页，可以直接在网页上填参数测接口。
- Windows + Python 3.14 环境下 uvicorn 的 `--reload` 热重载会崩溃，学习阶段不带 --reload 启动，改完代码手动 Ctrl+C 重启即可。
- 端口被占用时报 Errno 10048，可以用 `--port 8001` 换端口绕过。

## 十二、异步编程

- 异步接口用 `async def` 定义，函数体内调用异步操作用 `await`。
- 异步版 OpenAI 客户端用 `AsyncOpenAI`，调用方式是 `await client.chat.completions.create(...)`。
- 在 async 函数里使用同步阻塞调用会堵死整个事件循环，异步环境里必须配套用异步客户端。

## 十三、练习项目清单

- day19：第一个大模型 API 调用程序。
- day20：Prompt Engineering 练习（day20_prompts.py）。
- day21：temperature 参数实验 + ReAct 模式初体验（day21_temperature.py、day21_react.py）。
- day22：Embedding 余弦相似度实验（day22_similarity.py）+ 语义检索 TopK（day22_search.py）。
- day23：完整 RAG 文档问答工具（day23_rag.py + knowledge.txt），6 段文档检索 Top3 后交给 qwen-turbo 生成回答。
- day24：FastAPI 三个练习（day24_hello.py 入门、路径参数、day24_chat.py 对话 API），另写了异步版 day24_chat_asyn.py。
- day25：扣子 Coze 低代码平台搭建「个人知识助手」，用知识库实现平台版 RAG。

## 十四、个人踩坑记录

- `scored.append((score, doc))` 追加的是元组，括号不能漏，写成 `append(score, doc)` 会报 TypeError。
- uvicorn 启动命令里模块和 app 之间用冒号 `:`，不是点号 `.`。
- FastAPI 文件里容易漏写 `from fastapi import FastAPI`。
- f-string 三引号字符串容易漏掉 f 前缀，导致变量不生效。
- Git 提交前确认 `.env` 在 `.gitignore` 里，用 `git ls-files | grep .env` 检查密钥文件没有被跟踪。

---

> 本内容由 Coze AI 生成，请遵循相关法律法规及《人工智能生成合成内容标识办法》使用与传播。
