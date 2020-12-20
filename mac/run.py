#!/usr/bin/env python
# encoding:utf-8
from loguru import logger  # 导入日记库，没有请先安装 pip install loguru


# 为了保证性能，使用了 async await 开启异步，Python 3.7+ 的特性
async def hello_word(name):
    # 输出日记，生产环境会输出到指定目录
    logger.info("[Hello Word] 该 APP 执行参数为: {name}", name=name)
    # 返回值，格式为： 状态码，返回内容
    return {"status": 0, "result": "Hello," + name}


if __name__ == '__main__':
    # 导入异步库
    import asyncio

    # 测试函数
    async def test():
        status, result = await hello_word("W5")
        print(status, result)


    # 加入异步队列
    async def main(): await asyncio.gather(test())

    # 启动执行
    asyncio.run(main())
