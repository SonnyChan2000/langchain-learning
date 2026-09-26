# 让agent停下来等人工批准
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import interrupt, Command

class State(TypedDict):
    content: str
    approved: bool

def 生成内容(state: State):
    draft = "【系统生成】这是待发布的通知..."
    print(">> 已生成草稿, 等待人工审批")
    return {"content": draft}

def 人工审批(state: State) -> Command:
    """ HITL核心节点: 停下来问人工"""
    decision = interrupt({
        "question": "是否批准发布以下内容?",
        "content": state["content"],
        "options": ["approve", "reject"],
    })
    ok = (decision == "approve")
    print(f">>人工决定: {decision} -> {'批准' if ok else '驳回'}")
    return Command(goto="发布" if ok else "放弃", update={"approved": ok})

def 发布(state: State):
    print(">> 已发布")
    return {}

def 放弃(state: State):
    print(">> 已放弃发布")
    return {}

builder = StateGraph(State)
builder.add_node("生成", 生成内容)
builder.add_node("审批", 人工审批)
builder.add_node("发布", 发布)
builder.add_node("放弃", 放弃)
builder.add_edge(START, "生成")
builder.add_edge("生成", "审批")
builder.add_edge("发布", END)
builder.add_edge("放弃", END)

graph = builder.compile(checkpointer=InMemorySaver())

config = {"configurable": {"thread_id": "发布流程"}}
结果 = graph.invoke({"content": ""}, config)
print("\n第一次invoke返回(中断信息):")
print(结果["__interrupt__"])

人工答案 = input("请决定 approve 还是 reject: ")

继续 = graph.invoke(Command(resume=人工答案), config)
print("\n流程结束, approved =", 继续["approved"])