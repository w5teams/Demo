# !/usr/bin/env python
# encoding:utf-8
from loguru import logger  # 导入日记库，没有请先安装 pip install loguru


# 为了保证性能，使用了 async await 开启异步，Python 3.7+ 的特性
async def hello_world(name):
    # 输出日记，生产环境会输出到指定目录
    logger.info("[Hello Word] 该 APP 执行参数为: {name}", name=name)
    # 返回值，格式为： 状态码，返回内容
    return {"status": 0, "result": "Hello," + name}


# 下面代码可以用于测试使用
if __name__ == '__main__':
    import asyncio


    async def test():
        result = await hello_word("W5")
        print(result)


    asyncio.run(test())
