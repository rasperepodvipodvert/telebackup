from telethon import TelegramClient, events, sync
import argparse
import config

parser = argparse.ArgumentParser(description='Telegram backup bot')
parser.add_argument('-u', '--user_name', help='Example: @ifilatov')
parser.add_argument('-f', '--file_path', help='Example: /etc/passwd')
args = parser.parse_args()

if args.user_name:
    config.user_name = args.user_name
if args.file_path:
    config.file_path = args.file_path

api_id = config.api_id
api_hash = config.api_hash

client = TelegramClient(config.session_name, api_id, api_hash)
client.start()

client.send_file(config.user_name, config.file_path)