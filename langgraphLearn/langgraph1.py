from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# 1. 定义共享状态
class MyState(TypedDict):
    text: str

# 2. 定义节点函数
def step_a(state: MyState) -> dict:
    return {"text": state["text"] + " -> 经过节点A"}

def step_b(state: MyState) -> dict:
    return {"text": state["text"] + " -> 经过节点B"}

# 3. 构建图：添加节点和边
builder = StateGraph(MyState)
builder.add_node("a", step_a)
builder.add_node("b", step_b)
builder.add_edge(START, "a")
builder.add_edge("a", "b")
builder.add_edge("b", END)

# 4. 编译并运行
graph = builder.compile()
result = graph.invoke({"text": "开始"})
print(result["text"])