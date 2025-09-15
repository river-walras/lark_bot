"""
Lark Bot - 飞书自定义机器人推送库

这个包提供了同步和异步两种方式来发送飞书机器人消息。

同步使用方式:
    from larkbot_sdk import FeishuBot, create_bot_from_config, quick_log

异步使用方式:
    from larkbot_sdk.async_ import AsyncFeishuBot, create_bot_from_config, quick_log
"""

from .sync import FeishuBot, create_bot_from_config, quick_log
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
    "quick_log",
    "LarkBotError",
    "WebhookError",
    "AuthenticationError",
    "NetworkError",
    "MessageError",
]