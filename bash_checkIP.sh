#!/usr/bin/bash

#Program to tell it user-entered IP address is alive or not

echo "Enter IP addresses separated by space: "

#Reading an array of IP from user input
read -a ip_list
for i in ${ip_list[@]}; do
	echo "_______________________________"
	ping -c 1 -w 3 $i 2>&1 > /dev/null
  
	if [ $? -eq 0 ] ;
  	then
    		echo "Host $i is alive"
	else
  		echo "Host $i is down"
	fi
done
