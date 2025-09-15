"""Exception classes for lark_bot package."""


class LarkBotError(Exception):
    """Base exception for lark_bot package."""
    pass


class WebhookError(LarkBotError):
    """Exception raised for webhook-related errors."""
    pass


class AuthenticationError(LarkBotError):
    """Exception raised for authentication errors."""
    pass


class NetworkError(LarkBotError):
    """Exception raised for network-related errors."""
    pass


class MessageError(LarkBotError):
    """Exception raised for message formatting or sending errors."""
    pass