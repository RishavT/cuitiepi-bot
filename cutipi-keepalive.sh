#!/bin/bash
while true
do
	ping -c 1 google.com
	if [[ "$?" == "0" ]]
	then
		sudo systemctl status cutipi | grep active | grep -v inactive
		if [[ "$?" != "0" ]]
		then
			sudo systemctl start cutipi
		fi
	fi
	sleep 10s
done
