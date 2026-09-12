import operator

from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from langgraph.checkpoint.memory import InMemorySaver


class AgentState(TypedDict):

    history: Annotated[
        list[str],
        operator.add
    ]


def work(state: AgentState):

    return {
        "history": [
            "Agent 执行了一次 work"
        ]
    }


builder = StateGraph(AgentState)

builder.add_node(
    "work",
    work
)

builder.add_edge(
    START,
    "work"
)

builder.add_edge(
    "work",
    END
)


checkpointer=InMemorySaver()

graph = builder.compile(
    checkpointer=checkpointer
)


config={
    "configurable":{
        "thread_id":"agent-session-001",
    }
}


result = graph.invoke(
    {
        "history": [
            "用户：第一次任务"
        ]
    },
    config,
)


print(result)


# config2 = {
#     "configurable": {
#         "thread_id": "agent-session-002"
#     }
# }


result = graph.invoke(
    {
        "history": [
            "用户：第二次任务"
        ]
    },
    config,
)
print("restul two")
print(result)

state=graph.get_state(config)
print("state values:")
print(
    state.values
)

history = graph.get_state_history(
    config
)

for snapshot in history:
    print(snapshot.values)