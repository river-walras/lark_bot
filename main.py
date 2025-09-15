"""
演示 larkbot 包的使用方法，包括同步和异步版本
"""

import asyncio
import time

# 同步版本导入
from larkbot import FeishuBot, create_bot_from_config, quick_log

# 异步版本导入
from larkbot.async_ import AsyncFeishuBot
import larkbot.async_ as async_larkbot


def demo_sync_usage():
    """演示同步版本的使用方法"""
    # 配置信息 (示例，实际使用时请替换为真实的webhook和secret)
    WEBHOOK_URL = "your_webhook_url_here"
    SECRET = "your_secret_here"

    print("=== 同步版本演示 ===")

    # 方法1: 使用上下文管理器
    print("1. 使用上下文管理器...")
    try:
        with FeishuBot(WEBHOOK_URL, SECRET) as bot:
            result = bot.send_log_message("INFO", "系统正常启动，所有服务已就绪")
            print(f"发送结果: {result}")
    except Exception as e:
        print(f"发送失败: {e}")

    time.sleep(1)

    # 方法2: 手动管理生命周期
    print("2. 手动管理生命周期...")
    try:
        bot = FeishuBot(WEBHOOK_URL, SECRET)
        result = bot.send_log_message("WARN", "内存使用率达到85%，建议检查资源使用情况")
        print(f"发送结果: {result}")
        bot.close()
    except Exception as e:
        print(f"发送失败: {e}")

    time.sleep(1)

    # 方法3: 使用工厂函数
    print("3. 使用工厂函数...")
    try:
        bot = create_bot_from_config(WEBHOOK_URL, SECRET)
        result = bot.send_log_message("ERROR", "数据库连接失败，正在尝试重连...")
        print(f"发送结果: {result}")
        bot.close()
    except Exception as e:
        print(f"发送失败: {e}")

    time.sleep(1)

    # 方法4: 快速发送
    print("4. 快速发送...")
    try:
        result = quick_log(WEBHOOK_URL, "DEBUG", "这是一条通过快速接口发送的调试消息", SECRET)
        print(f"发送结果: {result}")
    except Exception as e:
        print(f"发送失败: {e}")


async def demo_async_usage():
    """演示异步版本的使用方法"""
    # 配置信息 (示例，实际使用时请替换为真实的webhook和secret)
    WEBHOOK_URL = "your_webhook_url_here"
    SECRET = "your_secret_here"

    print("\n=== 异步版本演示 ===")

    # 方法1: 使用异步上下文管理器
    print("1. 使用异步上下文管理器...")
    try:
        async with AsyncFeishuBot(WEBHOOK_URL, SECRET) as bot:
            result = await bot.send_log_message("INFO", "异步系统正常启动，所有服务已就绪")
            print(f"发送结果: {result}")
    except Exception as e:
        print(f"发送失败: {e}")

    await asyncio.sleep(1)

    # 方法2: 手动管理异步生命周期
    print("2. 手动管理异步生命周期...")
    try:
        bot = AsyncFeishuBot(WEBHOOK_URL, SECRET)
        result = await bot.send_log_message("WARN", "异步: 内存使用率达到85%")
        print(f"发送结果: {result}")
        await bot.aclose()
    except Exception as e:
        print(f"发送失败: {e}")

    await asyncio.sleep(1)

    # 方法3: 使用异步工厂函数
    print("3. 使用异步工厂函数...")
    try:
        bot = async_larkbot.create_bot_from_config(WEBHOOK_URL, SECRET)
        result = await bot.send_log_message("ERROR", "异步: 数据库连接失败")
        print(f"发送结果: {result}")
        await bot.aclose()
    except Exception as e:
        print(f"发送失败: {e}")

    await asyncio.sleep(1)

    # 方法4: 异步快速发送
    print("4. 异步快速发送...")
    try:
        result = await async_larkbot.quick_log(
            WEBHOOK_URL, "DEBUG", "这是一条异步快速发送的调试消息", SECRET
        )
        print(f"发送结果: {result}")
    except Exception as e:
        print(f"发送失败: {e}")

    # 方法5: 并发发送多条消息
    print("5. 并发发送多条消息...")
    try:
        tasks = []
        async with AsyncFeishuBot(WEBHOOK_URL, SECRET) as bot:
            for i in range(3):
                task = bot.send_log_message("INFO", f"并发消息 {i+1}")
                tasks.append(task)

            results = await asyncio.gather(*tasks, return_exceptions=True)
            for i, result in enumerate(results):
                print(f"消息 {i+1} 结果: {result}")
    except Exception as e:
        print(f"并发发送失败: {e}")


def main():
    """主函数，演示同步和异步使用方法"""
    print("Lark Bot 使用演示")
    print("=" * 50)

    # 演示同步使用
    demo_sync_usage()

    # 演示异步使用
    asyncio.run(demo_async_usage())

    print("\n演示完成！")
    print("\n使用说明:")
    print("- 同步版本: from larkbot import FeishuBot, create_bot_from_config, quick_log")
    print("- 异步版本: from larkbot.async_ import AsyncFeishuBot, create_bot_from_config, quick_log")
    print("- 请将示例中的 WEBHOOK_URL 和 SECRET 替换为实际的飞书机器人配置")


if __name__ == "__main__":
    main()
