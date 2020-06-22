#!/bin/bash
mkdir temp
cd temp
curl https://github.com/tmate-io/tmate/releases/download/2.4.0/tmate-2.4.0-static-linux-arm32v7.tar.xz -O -L
tar -xvf tmate-2.4.0-static-linux-arm32v7.tar.xz
cd tmate-2.4.0-static-linux-arm32v7
cp tmate /usr/local/sbin
chmod +x /usr/local/sbin/tmate
