from telethon import TelegramClient, events, sync
import argparse
import config

parser = argparse.ArgumentParser(description='Telegram backup bot')
parser.add_argument('-u', '--peer', help='Example: @ifilatov or channel name')
parser.add_argument('-f', '--file_path', help='Example: readme.md')
parser.add_argument('-c', '--caption', help='Example: Test File')
args = parser.parse_args()

if args.peer:
    config.peer = args.peer
if args.file_path:
    config.file_path = args.file_path
if args.caption:
    config.caption = args.caption

api_id = config.api_id
api_hash = config.api_hash
chat = None

client = TelegramClient(config.session_name, api_id, api_hash)
client.start()

if config.peer.startswith('@') or config.peer.startswith('me'):
    chat = client.get_entity(config.peer)
elif config.peer.startswith('-'):
    chat = client.get_peer_id(int(config.peer))

# send video file to telegramm channel
with open(config.file_path, 'rb') as f:
    client.send_file(chat, f, caption=config.caption)

# close program
client.disconnect()