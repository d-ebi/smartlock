#!/bin/bash

mkdir -p ${SMARTLOCK_APP_ROOT}/../log
echo "close" > ${SMARTLOCK_APP_ROOT}/.lock_status

pushd ${SMARTLOCK_APP_ROOT}
nohup python3 server.py >> ../log/app.log 2>&1 & 
popd

pushd ${SMARTLOCK_APP_ROOT}/../slackbot
nohup python3 run.py >> ../log/slackbot.log 2>&1 & 
popd
