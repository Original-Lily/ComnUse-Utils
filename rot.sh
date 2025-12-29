#!/bin/bash

SCREEN_NAME="HDMI-1"
ORIENTATION="right"
if xrandr | grep "$SCREEN_NAME connected"; then
    xrandr --output "$SCREEN_NAME" --rotate "$ORIENTATION"
else
    echo "Screen $SCREEN_NAME not found."
fi