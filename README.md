# CutiPi

A Telegram bot for Raspberry Pi. Does simple things.

Made with <3 by Rishav Thakker.

## Installation

### Requirements
* python3
* python-telegram-bot (You can install with pip or using your system's package manager)

1. Register a new bot on telegram
2. Update `config.json` and put your Telegram's Auth Token there
3. Also add a password for running commands (see below)
4. run `sudo bash install.sh`
5. reboot your Pi

## Commands

1. /hello
2. /ip - gives your pi's WiFi IP
3. /ssid - gives your pi's WIFI SSID
4. /command - let's you run a command from the internet. Use with caution. You can set your
    password in config.json for this.
