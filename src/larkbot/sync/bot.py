"""Synchronous FeishuBot implementation using httpx."""

import json
from typing import Dict, Optional

import httpx

from ..common import (
    ResponseResult,
    LogLevel,
    generate_sign,
    get_current_timestamp,
    get_level_config,
    build_log_content,
)
from ..exceptions import WebhookError, NetworkError, MessageError


class FeishuBot:
    """飞书自定义机器人推送类 (同步版本)"""

    def __init__(self, webhook_url: str, secret: Optional[str] = None):
        """
        初始化飞书机器人

        Args:
            webhook_url: 机器人Webhook地址
            secret: 安全密钥，可选

        Raises:
            WebhookError: 当webhook_url为空时
        """
        if not webhook_url:
            raise WebhookError("Webhook URL不能为空")

        self.webhook_url = webhook_url
        self.secret = secret
        self.client = httpx.Client(
            headers={"Content-Type": "application/json"},
            timeout=10.0
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        """关闭HTTP客户端"""
        self.client.close()

    def _send_message(self, msg_data: Dict) -> ResponseResult:
        """
        发送消息的底层方法

        Args:
            msg_data: 消息数据

        Returns:
            响应结果

        Raises:
            NetworkError: 网络请求错误
            MessageError: 消息发送错误
        """
        timestamp = get_current_timestamp()
        msg_data["timestamp"] = timestamp

        if self.secret:
            sign = generate_sign(timestamp, self.secret)
            msg_data["sign"] = sign

        try:
            response = self.client.post(
                self.webhook_url,
                content=json.dumps(msg_data)
            )
            response.raise_for_status()

            result = response.json()

            if result.get("code") != 0:
                error_msg = result.get("msg", "未知错误")
                print(f"发送失败：{error_msg}")
                raise MessageError(f"发送失败：{error_msg}")

            print("消息发送成功")
            return {"success": True, "error": None, "data": result}

        except httpx.HTTPStatusError as e:
            error_msg = f"HTTP错误 {e.response.status_code}: {e.response.text}"
            print(error_msg)
            raise NetworkError(error_msg) from e

        except httpx.RequestError as e:
            error_msg = f"网络请求错误: {str(e)}"
            print(error_msg)
            raise NetworkError(error_msg) from e

        except json.JSONDecodeError as e:
            error_msg = f"JSON解析错误: {str(e)}"
            print(error_msg)
            raise MessageError(error_msg) from e

        except Exception as e:
            error_msg = f"发送失败: {str(e)}"
            print(error_msg)
            raise MessageError(error_msg) from e

    def send_log_message(self, level: LogLevel, info: str) -> ResponseResult:
        """
        发送带有日志级别的富文本消息

        Args:
            level: 日志级别 (WARN, ERROR, INFO, DEBUG)
            info: 信息内容

        Returns:
            发送结果

        Raises:
            MessageError: 消息构建或发送错误
        """
        try:
            config = get_level_config(str(level))
            content = build_log_content(info)

            msg_data = {
                "msg_type": "post",
                "content": {
                    "post": {
                        "zh_cn": {
                            "title": f"{config['icon']} {str(level).upper()}",
                            "content": content,
                        }
                    }
                },
            }
            return self._send_message(msg_data)

        except Exception as e:
            error_msg = f"构建日志消息失败: {str(e)}"
            raise MessageError(error_msg) from e