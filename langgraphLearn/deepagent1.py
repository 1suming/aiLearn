import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

from langchain_openai import ChatOpenAI
from deepagents import create_deep_agent 

model=ChatOpenAI(
    model="glm-5.3-flash", 
    api_key=os.getenv("GLM_API_KEY", ""),
    base_url="https://open.bigmodel.cn/api/coding/paas/v4",

)

def get_weather(city:str) -> str:
    """get weather for a given city """
    return f"It's always sunny in {city}!"



agent=create_deep_agent(
    model=model,
    tools=[get_weather],
    system_prompt="you are a helpful assistant.",
)

result=agent.invoke(
    {"messages": [{"role":"user","content":"北京今天天气怎么样"}]}
)
print("你好")
print(result["messages"][-1].content)
