import asyncio 

async def fetch_data():
    print("开始请求:")
    await asyncio.sleep(2)
    print("请求完成")
    return "数据"
async def main():
    data=await fetch_data()
    print("结果::",data)

asyncio.run(main())    