import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

# ===== LangSmith 追踪开关 =====
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY", "")  # 在 smith.langchain.com 创建，通过环境变量注入
os.environ["LANGSMITH_PROJECT"] = "aiLearn"          # 可选,默认 default
# =============================

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



