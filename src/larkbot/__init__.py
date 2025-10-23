"""
Lark Bot - 飞书自定义机器人推送库

这个包提供了同步和异步两种方式来发送飞书机器人消息。

同步使用方式:
    from larkbot import FeishuBot, create_bot_from_config, set_url, quick_log

    # 设置全局URL，之后quick_log就不需要webhook_url参数
    set_url("https://your-webhook-url", "your-secret")
    quick_log(LogLevel.INFO, "消息内容")

异步使用方式:
    from larkbot.async_ import AsyncFeishuBot, create_bot_from_config, set_url, quick_log

    # 设置全局URL，之后quick_log就不需要webhook_url参数
    set_url("https://your-webhook-url", "your-secret")
    await quick_log(LogLevel.INFO, "消息内容")
"""

from .sync import FeishuBot, create_bot_from_config, set_url, quick_log
from .async_ import (
    AsyncFeishuBot,
    create_bot_from_config as create_async_bot_from_config,
    set_url as async_set_url,
    quick_log as async_quick_log,
)
from .exceptions import (
    LarkBotError,
    WebhookError,
    AuthenticationError,
    NetworkError,
    MessageError,
)

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

__all__ = [
    "FeishuBot",
    "create_bot_from_config",
    "set_url",
    "quick_log",
    "LarkBotError",
    "WebhookError",
    "AuthenticationError",
    "NetworkError",
    "MessageError",
    "AsyncFeishuBot",
    "create_async_bot_from_config",
    "async_set_url",
    "async_quick_log",
]
