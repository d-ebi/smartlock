# setup
## environment variables
```shell
$ echo "export SLACKBOT_TOKEN='{Your slackbot token}'" >> ~/.profile
$ echo "export SMARTLOCK_APP_ROOT='/home/pi/src/smartlock/app'" >> ~/.profile #example
$ source ~/.profile
```

## clone
```shell
$ git clone git@github.com:d-ebi/smartlock.git
$ cd smartlock
$ pip3 install -r requirements.txt
```

# boot
```shell
$ cd smartlock/bin
$ bash start.sh
```

# terminate
```shell
$ cd smartlock/bin
$ bash stop.sh
```
