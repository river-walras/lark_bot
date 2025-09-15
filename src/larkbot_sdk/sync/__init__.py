"""Synchronous FeishuBot implementation."""

from typing import Optional

from .bot import FeishuBot
from ..common import ResponseResult, LogLevel


def create_bot_from_config(webhook_url: str, secret: Optional[str] = None) -> FeishuBot:
    """
    从配置创建机器人实例

    Args:
        webhook_url: Webhook地址
        secret: 安全密钥

    Returns:
        FeishuBot实例
    """
    return FeishuBot(webhook_url, secret)


def quick_log(
    webhook_url: str,
    level: LogLevel,
    message: str,
    secret: Optional[str] = None
) -> ResponseResult:
    """
    快速发送日志消息（不需要创建实例）

    Args:
        webhook_url: Webhook地址
        level: 日志级别 (WARN, ERROR, INFO, DEBUG)
        message: 消息内容
        secret: 安全密钥

    Returns:
        发送结果
    """
    with FeishuBot(webhook_url, secret) as bot:
        return bot.send_log_message(level, message)


__all__ = [
    "FeishuBot",
    "create_bot_from_config",
    "quick_log",
]