#!/bin/bash
# Pre requisites:
# 1. Install python-telegram-bot
bash install-tmate.sh
cp ./*.sh ./*.py *.json /usr/local/sbin
cp ./*.service /usr/lib/systemd/system
systemctl enable cutipi-keepalive
