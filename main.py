from telethon import TelegramClient, events, sync
import config

api_id = config.api_id
api_hash = config.api_hash

client = TelegramClient(config.session_name, api_id, api_hash)
client.start()

client.send_file(config.user_name, 'requirements.txt')