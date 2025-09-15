"""Utility functions for lark_bot package."""

import base64
import hashlib
import hmac
from datetime import datetime
from typing import Dict

from .types import LevelConfig, LogLevel


def generate_sign(timestamp: int, secret: str) -> str:
    """
    Generate signature for authentication.

    Args:
        timestamp: Unix timestamp
        secret: Secret key for signing

    Returns:
        Base64 encoded signature
    """
    if not secret:
        return ""

    string_to_sign = f"{timestamp}\n{secret}"
    hmac_code = hmac.new(
        string_to_sign.encode("utf-8"), digestmod=hashlib.sha256
    ).digest()
    return base64.b64encode(hmac_code).decode("utf-8")


def get_current_timestamp() -> int:
    """Get current Unix timestamp."""
    return int(datetime.now().timestamp())


def get_formatted_timestamp() -> str:
    """Get formatted timestamp string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_level_config(level: LogLevel) -> LevelConfig:
    """
    Get configuration for log level.

    Args:
        level: Log level (INFO, WARN, ERROR, DEBUG)

    Returns:
        Level configuration with icon and color
    """
    level_configs = {
        "WARN": {"icon": "⚠️", "color": "#FF8C00"},
        "ERROR": {"icon": "❌", "color": "#FF4444"},
        "INFO": {"icon": "ℹ️", "color": "#007BFF"},
        "DEBUG": {"icon": "🐛", "color": "#6C757D"},
    }
    return level_configs.get(str(level).upper(), {"icon": "📝", "color": "#000000"})


def build_log_content(info: str) -> list[list[Dict[str, str]]]:
    """
    Build rich text content for log messages.

    Args:
        info: Information content

    Returns:
        Rich text content structure
    """
    timestamp = get_formatted_timestamp()
    return [
        [{"tag": "text", "text": info}],
        [{"tag": "text", "text": f"⏰ {timestamp}"}],
    ]