from typing_extensions import TypedDict 
from langgraph.graph import StateGraph,START,END

class AgentState(TypedDict):
    topic: str 
    research_result: str 
    final_answer: str 



def prepare(state: AgentState):
    return {
        "research_result": f"准备研究:{ state['topic']}"
    }

def research(state: AgentState):
    return {
            "research_result": f"{state['topic']} 是一种让 LLM 自主调用工具完成任务的系统。"
    }


def finish(state:AgentState):
    return {
        "final_answer":  f"最终研究结果：{state['research_result']}"
    }


builder=StateGraph(AgentState)
builder.add_node("prepare",prepare)
builder.add_node("research",research)
builder.add_node("finish",finish)

builder.add_edge(START,"prepare")
builder.add_edge("prepare", "research")
builder.add_edge("research", "finish")
builder.add_edge("finish", END)


graph= builder.compile()

result=graph.invoke({
      "topic": "AI Agent",
    "research_result": "",
    "final_answer": ""
})

print(result)
