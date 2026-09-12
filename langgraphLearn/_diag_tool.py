"""诊断:打印 agent 完整消息轨迹,确认 get_weather 是否被调用"""
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

from langchain_openai import ChatOpenAI
from deepagents import create_deep_agent

model = ChatOpenAI(
    model="glm-5.3-flash",
    api_key=os.getenv("GLM_API_KEY", ""),
    base_url="https://open.bigmodel.cn/api/coding/paas/v4",
)


def get_weather(city: str) -> str:
    """get weather for a given city"""
    return f"It's always sunny in {city}!"


agent = create_deep_agent(
    model=model,
    tools=[get_weather],
    system_prompt="you are a helpful assistant.",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "北京今天天气怎么样"}]}
)

for i, m in enumerate(result["messages"]):
    mtype = m.__class__.__name__
    tool_calls = getattr(m, "tool_calls", None)
    name = getattr(m, "name", "")
    content = str(m.content)[:120].replace("\n", " ")
    print(f"[{i}] {mtype} name={name!r} tool_calls={[tc['name'] for tc in tool_calls] if tool_calls else None}")
    print(f"    content: {content}")
