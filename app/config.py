import os

# SSL settings
SSL_DIR = os.getenv('SSL_DIR')
SSL_CERT = os.getenv('SSL_CERT')
SSL_PRIV = os.getenv('SSL_PRIV')

# Telegram token
TGBOT_TOKEN = os.getenv('TGBOT_TOKEN')

# Telegram admins ID
TG_ADMINS_ID = [int(ID) for ID in os.getenv('TG_ADMINS_ID').split(':')]

# Telegram webhook
WEBHOOK_HOST = os.getenv('WEBHOOK_HOST')
WEBHOOK_PORT = os.getenv('WEBHOOK_PORT')
WEBHOOK_PATH = os.getenv('WEBHOOK_PATH')

# Webhost
WEBAPP_HOST = os.getenv('WEBAPP_HOST')
WEBAPP_PORT = os.getenv('WEBAPP_PORT')

# Group id
TG_OBSERVED_GROUP_ID = os.getenv('TG_OBSERVED_GROUP_ID')

# Channel id
TG_MANAGED_CHANNEL_ID = os.getenv('TG_MANAGED_CHANNEL_ID')
