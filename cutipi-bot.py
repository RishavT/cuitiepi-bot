import time
import os
import json
from telegram.ext import Updater, CommandHandler, Filters

CONFIG = json.loads(open(os.path.join('/usr/local/sbin/config.json')).read())
COMMAND_PASSWORD = CONFIG['command_password']
TELEGRAM_TOKEN = CONFIG['telegram_token']

def get_ssid():
    command_out = os.popen("iwgetid| grep wlan").read().strip()
    ssid = command_out.split("ESSID")[1].split(":")[1].replace('"', '')
    return ssid

def get_wifi_ip():
    command_out = os.popen("ip addr | grep wlan | grep inet").read().strip()
    ip = command_out.split(" ")[1].split("/")[0]
    return ip

def get_ip():
    try:
        return get_wifi_ip()
    except Exception as e:
        return os.popen("ip addr").read()

def hello(update, context):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def ssid(update, context):
    update.message.reply_text(
        f'I am connected to: {get_ssid()}')

def run_command(update, context):
    args = context.args
    if len(args) < 2:
        update.message.reply_text(
            "Usage: `/command <secret> <your command here>")
        return

    password = args[0]
    command = " ".join(args[1:])
    if password == COMMAND_PASSWORD:
        out = os.popen(command).read()
        update.message.reply_text(out)
    else:
        update.message.reply_text("Invalid secret")

def test_error(update, context):
    a = 1
    b = 0
    c = a/b
    
def ip(update, context):
    update.message.reply_text(
        f'My IP is {get_ip()}')


def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    
    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.dispatcher.add_handler(CommandHandler('ip', ip))
    updater.dispatcher.add_handler(CommandHandler('ssid', ssid))
    updater.dispatcher.add_handler(CommandHandler('test_error', test_error))
    updater.dispatcher.add_handler(CommandHandler('command', run_command))
    print("Running")
    
    updater.start_polling()
    updater.idle()
    print("Exiting")

if __name__ == "__main__":
    main()

