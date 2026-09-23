import operator
from typing_extensions import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    question: str
    need_tool: bool
    answer: str
    steps: Annotated[list, operator.add]

def 分析问题(state: State):
    q = state["question"]
    print(">>> 分析问题:", q)
    need_tool = any(k in q for k in ["计算", "查", "算"])
    return {"need_tool": need_tool, "steps": ["分析"]}

def 调用工具(state: State):
    print(">>> 调用工具节点: 帮你查询/计算")
    return {"answer": f"已用工具处理: {state['question']}", "steps": ["工具"]}

def 直接回答(state: State):
    print(">>> 直接回答节点: 知识库直接答")
    return {"answer": f"直接回答 {state['question']}", "steps": ["直接答"]}

def 路由(state: State) -> str:
    """条件函数: 决定下一步去哪个节点(核心!)"""
    return "工具" if state.get("need_tool", False) else "直接答"

builder = StateGraph(State)
builder.add_node("分析", 分析问题)
builder.add_node("工具", 调用工具)
builder.add_node("直接答", 直接回答)
builder.add_edge(START, "分析")
# 条件边
builder.add_conditional_edges("分析", 路由, {"工具": "工具", "直接答": "直接答"})
builder.add_edge("工具", END)
builder.add_edge("直接答", END)
graph = builder.compile()

for q in ["帮我查一下天气", "你好"]:
    结果 = graph.invoke({"question": q})
    print(f"\n问题'{q}' -> 结果: {结果['answer']}, 路径: {结果['steps']}")