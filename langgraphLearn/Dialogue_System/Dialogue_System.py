
"""
智能搜索助手 - 基于 LangGraph + Tavily API 的真实搜索系统
1. 理解用户需求
2. 使用Tavily API真实搜索信息  
3. 生成基于搜索结果的回答
"""

import asyncio
from typing import TypedDict, Annotated
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver
import os
from dotenv import load_dotenv
from tavily import TavilyClient


async def main():
    app=create_search_assistant()
    print("🔍 智能搜索助手启动！")
    print("我会使用Tavily API为您搜索最新、最准确的信息")
    print("支持各种问题：新闻、技术、知识问答等")
    print("(输入 'quit' 退出)\n")

    session_count=0

    while True:
        user_input = input("🤔 您想了解什么: ").strip()
        if user_input.lower() in ['quit', 'q', '退出', 'exit']:
            print("感谢使用！再见！👋")
            break
        if not user_input:
            continue
        session_count += 1
        config= {"configurable": {"thread_id": f"search-session-{session_count}"}}

        # 初始状态
        initial_state= {
            "messages": [ HumanMessage(content=user_input)],
            "user_query":"",
            "search_query":"",
            "search_results":"",
            "final_answer":"",
            "step":"start",
        }

        try:
            print("\n" + "="*60)

            async for output in app.astream(initial_state,config=config):
                for node_name,node_output in output.items():
                    if "messages" in node_output and node_output["messages"]:
                        latest_message=node_output["messages"][-1]
                        if isinstance(latest_message,AIMessage):
                            if node_name=="understand":
                                print(f"🧠 理解阶段: {latest_message.content}")
                            elif node_name == "search":
                                print(f"🔍 搜索阶段: {latest_message.content}")
                            elif node_name == "answer":
                                print(f"\n💡 最终回答:\n{latest_message.content}")

                print("\n" + "="*60 + "\n")
        except Exception as e:
            print(f"❌ 发生错误: {e}")
            print("请重新输入您的问题。\n")

        

if __name__ == "__main__":
    asyncio.run(main())

            