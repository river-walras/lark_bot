"""Type definitions for lark_bot package."""

from typing import Dict, Any, TypedDict, Optional, Literal


class ResponseResult(TypedDict):
    """Standard response result structure."""
    success: bool
    error: Optional[str]
    data: Optional[Dict[str, Any]]


class PostContent(TypedDict):
    """Post message content structure."""
    title: str
    content: list[list[Dict[str, str]]]


class PostMessage(TypedDict):
    """Post message structure for zh_cn."""
    zh_cn: PostContent


class MessageData(TypedDict):
    """Base message data structure."""
    msg_type: str
    timestamp: Optional[int]
    sign: Optional[str]


class PostMessageData(MessageData):
    """Post message data structure."""
    content: Dict[str, PostMessage]


class LevelConfig(TypedDict):
    """Log level configuration."""
    icon: str
    color: str


# Type aliases
MessageResponse = Dict[str, Any]
LogLevel = Literal["INFO", "WARN", "ERROR", "DEBUG"]