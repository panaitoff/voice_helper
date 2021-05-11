import speech_recognition as sr
from pyowm.utils.config import get_default_config
import pyttsx3
import sys
import webbrowser
import pyowm
import eel
from pygame import mixer
import time
import locale


@eel.expose
def speak(what):
    engine = pyttsx3.init()
    engine.say(what)
    engine.runAndWait()

    return what


# @eel.expose
# def makeSomething():
#     r = sr.Recognizer()
#     m = sr.Microphone(device_index=1)
#
#     with m as source:
#         r.adjust_for_ambient_noise(source)
#
#     # Обработка голоса пользователя
#
#     r = sr.Recognizer()
#
#     with sr.Microphone() as source:
#         print("Говорите")
#         r.pause_threshold = 1
#         r.adjust_for_ambient_noise(source, duration=1)
#         audio = r.listen(source)
#
#     try:
#         zadanie = r.recognize_google(audio, language="ru-RU")
#         print("Вы сказали: " + zadanie)
#
#     except sr.UnknownValueError:
#         return "Я вас не поняла"
#         zadanie = makeSomething()
#
#     # для it-куба
#     # zadanie = input()
#
#     return zadanie.lower()


@eel.expose
def command(task):
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

    if 'день' or ('какое' and 'число') in task:
        return day

    elif 'погода' in task:
        return f'Температура в {place} сейчас в районе {int(temp)} градусов, {cloud}'

    elif 'время' or 'час' in task:
        return times

    else:
        url = f'https://www.google.com/search?q={task}'
        webbrowser.open(url)


if __name__ == '__main__':
    eel.init('web')
    eel.start('main.html', size=(570, 620))
