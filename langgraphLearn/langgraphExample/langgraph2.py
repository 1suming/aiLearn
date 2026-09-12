from typing_extensions import TypedDict 
from langgraph.graph import StateGraph,START,END

class AgentState(TypedDict):
    topic: str 
    research_count:int
    research_result: str 
    final_answer: str 



# def prepare(state: AgentState):
#     return {
#         "research_result": f"准备研究:{ state['topic']}"
#     }

def research(state: AgentState):
    new_count=state["research_count"]+1
    return {
        "research_count": new_count,
        "research_result": f"第 {new_count} 次研究 {state['topic']}"
    }
    # return {
    #         "research_result": f"{state['topic']} 是一种让 LLM 自主调用工具完成任务的系统。"
    # }

def should_continue(state:AgentState):
    if state["research_count"]>=3:
        return "finish"
    return "continue"


# def finish(state:AgentState):
#     return {
#         "final_answer":  f"最终研究结果：{state['research_result']}"
#     }
def finish(state: AgentState):

    return {
        "final_answer":
            f"{state['topic']} 已研究 {state['research_count']} 次，研究完成。"
    }

builder=StateGraph(AgentState)
# builder.add_node("prepare",prepare)
builder.add_node("research",research)
builder.add_node("finish",finish)

builder.add_edge(START,"research")
# builder.add_edge("research", "finish")

builder.add_conditional_edges(
    "research",
    should_continue, 
    {
        "continue":"research",
        "finish":"finish",
    }

)
builder.add_edge("finish", END)


graph= builder.compile()

result=graph.invoke({
      "topic": "AI Agent",
      "research_count":0,
    "research_result": "",
    "final_answer": ""
})

print(result)
