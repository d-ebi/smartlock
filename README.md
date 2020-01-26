# Setup
## Environment variables
```shell
$ echo "export SLACKBOT_TOKEN='{Your slackbot token}'" >> ~/.profile
$ echo "export SMARTLOCK_APP_ROOT='/home/pi/src/smartlock/app'" >> ~/.profile #example
$ source ~/.profile
```

## Clone and install library
```shell
$ git clone git@github.com:d-ebi/smartlock.git
$ cd ./smartlock
$ pip3 install -r requirements.txt
```

# Boot
```shell
$ cd ./bin
$ bash start.sh
```

# Terminate
```shell
$ cd ./bin
$ bash stop.sh
```

# Web UI
Access to `http://localhost:8080` or `http://{Your IP Address}:8080`

# Slackbot
You send mention or direct message to slackbot.

## example
### open
```
@slackbot_name open
or
@slackbot_name 開錠
```

### close
```
@slackbot_name close
or
@slackbot_name 施錠
```
