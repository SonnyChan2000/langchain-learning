import operator
from typing_extensions import TypedDict,Annotated
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    text: str
    steps: Annotated[list, operator.add]

def 节点一(state: State):
    print(">>>节点一执行, 收到:", state["text"])
    return {"text": state["text"] + "(已被节点一处理)", "steps":["节点一"]}

def 节点二(state: State):
    print(">>>节点二执行, 收到:", state["text"])
    return {"text": state["text"] + "(已被节点二处理)", "steps": ["节点二"]}

bulider = StateGraph(State)
bulider.add_node("节点一", 节点一)
bulider.add_node("节点二", 节点二)
bulider.add_edge(START, "节点一")
bulider.add_edge("节点一", "节点二")
bulider.add_edge("节点二", END)
graph = bulider.compile()

结果 = graph.invoke({"text": "你好", "steps":["入口"]})
print("\n最终 State:", 结果)


