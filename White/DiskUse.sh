#!/bin/bash
THRESHOLD=90
USAGE=$(df / | grep / | awk '{ print $5 }' | sed 's/%//g')
if [ $USAGE -gt $THRESHOLD ]; then
    echo "Disk usage is above $THRESHOLD%" | mail -s "Disk Usage Alert" user@example.com
fi
