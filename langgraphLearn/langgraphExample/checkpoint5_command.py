from typing_extensions import TypedDict

from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from langgraph.types import Command


class AgentState(TypedDict):
    task: str
    task_type: str
    result: str


def supervisor(state: AgentState):

    task = state["task"]

    if "代码" in task:

        return Command(
            update={
                "task_type": "coding"
            },
            goto="coder"
        )

    return Command(
        update={
            "task_type": "research"
        },
        goto="researcher"
    )


def coder(state: AgentState):

    return {
        "result":
            f"Coder 完成任务：{state['task']}"
    }


def researcher(state: AgentState):

    return {
        "result":
            f"Researcher 完成任务：{state['task']}"
    }


builder = StateGraph(AgentState)

builder.add_node(
    "supervisor",
    supervisor
)

builder.add_node(
    "coder",
    coder
)

builder.add_node(
    "researcher",
    researcher
)


builder.add_edge(
    START,
    "supervisor"
)

builder.add_edge(
    "coder",
    END
)

builder.add_edge(
    "researcher",
    END
)


graph = builder.compile()


result = graph.invoke({
    "task": "帮我写一段 Python 代码",
    "task_type": "",
    "result": ""
})


print(result)