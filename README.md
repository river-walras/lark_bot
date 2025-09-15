# Lark Bot

A Python library for sending messages to Feishu (Lark) custom bots, supporting both synchronous and asynchronous operations.

## Features

- 🔄 Both synchronous and asynchronous support
- 🚀 Simple and intuitive API design
- 🛡️ Comprehensive error handling with custom exception types
- 📝 Log-level message support
- ⚡ Batch and concurrent sending capabilities
- 🎯 Type-safe with full type hints
- 🔧 Global URL configuration for convenient quick logging

## Installation

```bash
pip install larkbot
```

## Quick Start

### Synchronous Usage

```python
from larkbot import FeishuBot, set_url, quick_log, LogLevel

# Configuration
WEBHOOK_URL = "your_feishu_bot_webhook_url"
SECRET = "your_feishu_bot_secret"

# Method 1: Using context manager (recommended)
with FeishuBot(WEBHOOK_URL, SECRET) as bot:
    result = bot.send_log_message(LogLevel.INFO, "System started successfully")
    print(result)

# Method 2: Quick send
result = quick_log(LogLevel.ERROR, "An error occurred", WEBHOOK_URL, SECRET)

# Method 3: Set URL globally then use quick_log (NEW!)
set_url(WEBHOOK_URL, SECRET)
result = quick_log(LogLevel.INFO, "No need to pass URL/secret every time!")
```

### Asynchronous Usage

```python
import asyncio
from larkbot.async_ import AsyncFeishuBot, set_url, quick_log, LogLevel

async def main():
    WEBHOOK_URL = "your_feishu_bot_webhook_url"
    SECRET = "your_feishu_bot_secret"

    # Using async context manager
    async with AsyncFeishuBot(WEBHOOK_URL, SECRET) as bot:
        result = await bot.send_log_message(LogLevel.INFO, "Async system started")
        print(result)

    # Async quick send
    result = await quick_log(LogLevel.WARN, "Warning message", WEBHOOK_URL, SECRET)

    # Set URL globally then use quick_log (NEW!)
    set_url(WEBHOOK_URL, SECRET)
    result = await quick_log(LogLevel.INFO, "No need to pass URL/secret every time!")

# Run async code
asyncio.run(main())
```

## API Documentation

### Synchronous API

#### FeishuBot

```python
from larkbot import FeishuBot, create_bot_from_config

# Direct instantiation
bot = FeishuBot(webhook_url, secret)

# Using factory function
bot = create_bot_from_config(webhook_url, secret)

# Send log message
result = bot.send_log_message(level, message)

# Close connection
bot.close()
```

#### Quick Send

```python
from larkbot import set_url, quick_log, LogLevel

# Method 1: Pass URL and secret each time
result = quick_log(LogLevel.INFO, "Message", webhook_url, secret)

# Method 2: Set globally, then use quick_log without URL/secret
set_url(webhook_url, secret)
result = quick_log(LogLevel.INFO, "Message")
```

### Asynchronous API

#### AsyncFeishuBot

```python
from larkbot.async_ import AsyncFeishuBot, create_bot_from_config

# Direct instantiation
bot = AsyncFeishuBot(webhook_url, secret)

# Using factory function
bot = create_bot_from_config(webhook_url, secret)

# Send log message
result = await bot.send_log_message(level, message)

# Close connection
await bot.aclose()
```

#### Async Quick Send

```python
from larkbot.async_ import set_url, quick_log, LogLevel

# Method 1: Pass URL and secret each time
result = await quick_log(LogLevel.INFO, "Message", webhook_url, secret)

# Method 2: Set globally, then use quick_log without URL/secret
set_url(webhook_url, secret)
result = await quick_log(LogLevel.INFO, "Message")
```

### Concurrent Sending Example

```python
import asyncio
from larkbot.async_ import AsyncFeishuBot

async def batch_send():
    async with AsyncFeishuBot(webhook_url, secret) as bot:
        tasks = [
            bot.send_log_message("INFO", f"Message {i}")
            for i in range(5)
        ]
        results = await asyncio.gather(*tasks)
        return results
```

## Log Levels

Supports the following log levels:

- `DEBUG` - Debug information
- `INFO` - General information
- `WARN` - Warning messages
- `ERROR` - Error messages

## Exception Handling

The library provides comprehensive exception types:

```python
from larkbot import (
    LarkBotError,          # Base exception
    WebhookError,          # Webhook related errors
    AuthenticationError,   # Authentication errors
    NetworkError,          # Network errors
    MessageError,          # Message format errors
)

try:
    with FeishuBot(webhook_url, secret) as bot:
        result = bot.send_log_message("INFO", "Test message")
except AuthenticationError:
    print("Authentication failed, check webhook and secret")
except NetworkError:
    print("Network connection failed")
except MessageError:
    print("Message format error")
```

## Requirements

- Python 3.9+
- Valid Feishu custom bot webhook URL
- Bot secret (if signature verification is enabled)

## Development

```bash
# Clone the repository
git clone <repository-url>
cd larkbot

# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Code formatting
black .
isort .

# Type checking
mypy .
```

## License

MIT License

## Contributing

Issues and Pull Requests are welcome!