import operator
from typing_extensions import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    current: int
    target: int
    steps: Annotated[list, operator.add]

def 初始(state: State):
    print(f">>> 初始: 现在是{state['current']}, 目标是{state['target']}")
    return {"steps": ["初始"]}

def 加一并检查(state: State):
    now = state["current"] + 1
    print(f">>>加一: {state['current']} + 1 = {now}")
    return {"current": now, "steps": [f"加一→{now}"]}

def 是否达标(state: State) -> str:
    """条件: 达标就END, 没达标就回到"加一并检查"(形成循环)"""
    if state["current"] >= state["target"]:
        return "达标"
    return "继续"

builder = StateGraph(State)
builder.add_node("初始", 初始)
builder.add_node("加一并检查", 加一并检查)
builder.add_edge(START, "初始")
builder.add_edge("初始", "加一并检查")
# 关键: 条件边让"加一并检查"可以回到自己(循环)或结束
builder.add_conditional_edges("加一并检查", 是否达标, {"继续": "加一并检查", "达标": END})
graph = builder.compile()

结果 = graph.invoke({"current": 0, "target": 3})
print(f"\n最终 current={结果['current']}, 执行路径={结果['steps']}")