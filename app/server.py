from bottle import route, run, template, static_file
from slacker import Slacker
import RPi.GPIO as GPIO
import json
import os
import requests
import time


slacker = Slacker(os.environ['SLACKBOT_TOKEN'])
SETTINGS = {
    'open': {
        'message': '<!channel>\n鍵を開けたよ:unlock:',
        'cycle'  : 12,
    },
    'close': {
        'message': '<!channel>\n鍵を閉めたよ:lock:',
        'cycle'  : 6.75
    }
}


def control_servo(cycle):
    GPIO.setmode(GPIO.BOARD)

    gp_out = 33
    GPIO.setup(gp_out, GPIO.OUT)

    servo = GPIO.PWM(gp_out, 50)
    servo.start(0)

    GPIO.setup(gp_out, GPIO.OUT)
    time.sleep(0.5)

    servo.ChangeDutyCycle(cycle)
    time.sleep(0.5)

    GPIO.cleanup(gp_out)


@route('/')
def index():
    return template('index')


@route('/api/1/lock/status')
def get_lock_status():
    with open('./.lock_status', mode='r') as f:
        status = f.read()

    return {'status': status}


@route('/api/1/lock/change/<status>')
def change_lock(status):
    with open('./.lock_status', mode='w') as f:
        f.write(status)

    setting = SETTINGS[status]

    control_servo(setting['cycle'])
    slacker.chat.post_message('#notify', setting['message'], as_user=True)

    return {'status': status}


@route('/api/1/lock/switch')
def switch_lock():
    with open('./.lock_status', mode='r') as f:
        status  = f.read()
        reverse = 'close' if status == 'open' else 'open'

    return change_lock(reverse)


@route('/<filename:path>')
def static(filename):
    app_root = os.environ['SMARTLOCK_APP_ROOT']
    return static_file(filename, root='{}/static'.format(app_root))


if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, reloader=True)
