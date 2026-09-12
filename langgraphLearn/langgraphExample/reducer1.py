from typing import Annotated
from typing_extensions import TypedDict
import operator

from langgraph.graph import StateGraph, START, END

class AgentState(TypedDict):
    topic: str 

    research_results: Annotated[list[str],operator.add] # list[str]    #

    status: str 


def github_search(state: AgentState):

    return {
        "research_results": [
            f"GitHub 搜索结果：{state['topic']}"
        ],
        "status": "github_finished"
    }


def reddit_search(state: AgentState):

    return {
        "research_results": [
            f"Reddit 搜索结果：{state['topic']}"
        ],
        "status": "reddit_finished"
    }


def finish(state: AgentState):

    print(
        "所有研究结果：",
        state["research_results"]
    )

    return {
        "status": "finished"
    }


builder = StateGraph(AgentState)

builder.add_node(
    "github",
    github_search
)

builder.add_node(
    "reddit",
    reddit_search
)

builder.add_node(
    "finish",
    finish
)

builder.add_edge(
    START,
    "github"
)

builder.add_edge(
    "github",
    "reddit"
)

builder.add_edge(
    "reddit",
    "finish"
)

builder.add_edge(
    "finish",
    END
)

graph = builder.compile()


result = graph.invoke({
    "topic": "Deep Agents",

    "research_results": [],

    "status": "started"
})


print(result)