from slackbot.bot import respond_to
import urllib.request


SETTINGS = {
    'open' : r'((鍵|かぎ)を*[開あ]けて|kagi(wo)*akete|開錠|open)',
    'close': r'((鍵|かぎ)を*([閉し]め|[掛か]け)て|kagi(wo)*sh*imete|施錠|close)'
}


def __call_change_lock(status):
    url = 'http://localhost:8080/api/1/lock/change/{}'.format(status)
    request = urllib.request.Request(url)
    urllib.request.urlopen(request)


@respond_to(SETTINGS['open'])
def open_lock(message, *group):
    __call_change_lock('open')


@respond_to(SETTINGS['close'])
def close_lock(message, *group):
    __call_change_lock('close')
