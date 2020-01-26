#!/bin/bash

ps aux | grep -E "python3 (server|run)\.py" | grep -v 'grep' | awk '{print $2}' | while read line
do
  kill ${line}
done
