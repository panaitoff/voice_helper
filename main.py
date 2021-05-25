import speech_recognition as sr
from pyowm.utils.config import get_default_config
import pyttsx3
import webbrowser
import pyowm
import eel
import time
import os
import locale


@eel.expose
def speak(what):
    engine = pyttsx3.init()
    engine.say(what)
    engine.runAndWait()

    return what


@eel.expose
def command(a):
    task = a

    locale.setlocale(locale.LC_ALL, 'Russian_Russia.1251')

    owm = pyowm.OWM('6f5dc1652adf891c89bf794c92ff3ba4')
    mgr = owm.weather_manager()

    place = 'Санкт-Петербург'

    config_dict = get_default_config()
    config_dict['language'] = 'ru'

    observation = mgr.weather_at_place(place)
    w = observation.weather

    temp = w.temperature('celsius')['temp']
    cloud = w.detailed_status

    day = time.strftime('Сейчас %d %B, %A')
    times = time.strftime('%H:%M')

    if ('день' or ('какое' and 'число')) in task:
        return day

    elif 'погода' in task:
        return f'Температура в {place} сейчас в районе {int(temp)} градусов, {cloud}'

    elif ('время' or 'час') in task:
        return times

    elif ('выключи' and 'компьютер') in task:
        os.system('shutdown -s')
        return 'Выключаю!'

    elif ('перезагрузи' and 'копмьютер') in task:
        os.system(['shutdown', '-r' '-t', '0'])
        return 'минуточку'

    elif 'открой' and ('ютуб' or 'youtube') in task:
        url = 'https://www.youtube.com'
        webbrowser.open(url)
        return 'открываю'

    elif 'открой' and ('gmail' or 'гмаил' or 'почту') in task:
        url = 'https://mail.google.com'
        webbrowser.open(url)
        return 'открываю'

    elif 'открой' and ('mail' or 'маил') in task:
        url = 'https://mail.ru'
        webbrowser.open(url)
        return 'открываю'

    elif 'открой' and ('twitch' or 'твич') in task:
        url = 'https://twitch.tv'
        webbrowser.open(url)
        return 'открываю'

    elif 'открой' and ('твитер' or 'твиттер' or 'twitter') in task:
        url = 'https://twitter.com'
        webbrowser.open(url)
        return 'открываю'

    elif 'открой' and ('вк' or 'вконтакте' or 'vk' or 'vkontakte') in task:
        url = 'https://vk.com'
        webbrowser.open(url)
        return 'открываю'

    elif 'открой' and ('инстаграмм' or 'инстаграм' or 'instagram' or 'инсту') in task:
        url = 'https://www.instagram.com/'
        webbrowser.open(url)
        return 'открываю'

    else:
        url = f'https://www.google.com/search?q={task}'
        webbrowser.open(url)


if __name__ == '__main__':
    eel.init('web')
    eel.start('main.html', size=(560, 690))
