import os


# this is the bot token, gotten from BotFather
TELEGRAM_BOT_TOKEN = os.environ.get("TOKEN")
# this is your own telegram ID, which is used to send exception tracebacks
DEVELOPER_CHAT_ID = os.environ.get("SUDO")
# list of telegram IDs for them /stats command is enabled
MAINTAINERS_CHAT_IDS = [DEVELOPER_CHAT_ID, ]