import speech_recognition as sr
from pyowm.utils.config import get_default_config
import pyttsx3
import sys
import webbrowser
import dictionary
import pyowm
import pesni
import eel
import random
from pygame import mixer
import time
import locale

locale.setlocale(locale.LC_ALL, 'Russian_Russia.1251')

eel.init('web')

eel.start('main.html', size=(600, 650))

# 6f5dc1652adf891c89bf794c92ff3ba4 API key OWM

cmd = dictionary.opts['cmd']['search']


# Голос помошника
def speak(what):
    print(what)
    engine = pyttsx3.init()
    engine.say(what)
    engine.runAndWait()


speak("Привет, чем я могу помочь вам?")


# r = sr.Recognizer()
# m = sr.Microphone(device_index=1)
#
# with m as source:
#     r.adjust_for_ambient_noise(source)


# Обработка голоса пользователя
def makeSomething():
    # r = sr.Recognizer()
    #
    # with sr.Microphone() as source:
    #     print("Говорите")
    #     r.pause_threshold = 1
    #     r.adjust_for_ambient_noise(source, duration=1)
    #     audio = r.listen(source)
    #
    # try:
    #     zadanie = r.recognize_google(audio, language="ru-RU")
    #     print("Вы сказали: " + zadanie)
    #
    # except sr.UnknownValueError:
    #     speak("Я вас не поняла")
    #     zadanie = makeSomething()

    # для it-куба
    zadanie = input()

    return zadanie.lower()


# Команды которые обрабатываются
def command(zadanie):
    global name, cmd, mistakes

    rnd = random.randint(0, 1)

    if 'что' and 'делает' and 'овца' in zadanie:
        speak('Я ебу. Ты видишь здесь зоолога?')

    if 'найди' in zadanie:
        st = ''
        a = zadanie.split(' ')
        a.pop(0)

        for i in range(len(a)):
            st += a[i]

        speak("Уже открываю")
        url = f'https://www.google.com/search?q={st}'
        webbrowser.open(url)

    if 'время' or 'час' in zadanie:
        speak(time.strftime('%H:%M'))

    if 'день' in zadanie:
        speak(time.strftime('Сейчас %d %B, %A'))

    if 'погода' in zadanie:
        speak(f'Температура в {place} сейчас в районе {int(temp)} градусов, {cloud}')
        print('Рекоменнации как одется: ')
        if int(temp) >= 10:
            speak('Можешь спокойно одеть кепку и стать репером как в одном анекдоте')
        elif 10 > int(temp) >= 5:
            speak('Придет надеть кофточку!')
        elif 5 > int(temp) >= 0:
            speak('Шапочку только надень, а так норм')
        elif 0 > int(temp) >= -5:
            speak('Куртка, шапка и тапки. И лети гулять')
        elif -5 > int(temp) >= -10:
            speak(f'СКОЛЬКО {int(temp)}. Тут даже я хз как одется')
        elif -10 > int(temp) >= -25:
            speak('Можно в принципе футбольку одеть')
        elif int(temp) <= -30:
            speak('Надеюсь ты не на северном полюсе?')

    elif 'новое имя' in zadanie:
        speak('Какое?')
        name = makeSomething()

    elif 'стоп' in zadanie:
        speak("Да, конечно, без проблем")
        sys.exit()

    elif 'имя' in zadanie:
        speak(name)

    elif 'спой' and 'песню' in zadanie:
        mixer.init()

        speak('А теперь как вы и просили песня \"Аллы Пугачёвой - Айсберг\"')

        mixer.music.load("music/айсберг.mp3")
        mixer.music.set_volume(0.12)
        mixer.music.play()

        time.sleep(40)

        speak('\nЛедяной горою айсберг из тумана вырастает'
              '\nИ несёт его теченье по бескрайним по морям'
              '\nХорошо тому, кто знает как опасен в океане'
              '\nКак опасен в океане айсберг встречным кораблям')

        speak('\nА я про всё на свете с тобою забываю'
              '\nА я в любовь, как в море, бросаюсь с головой'
              '\nА ты такой холодный как айсберг в океане'
              '\nИ все твои печали под чёрною водой'
              '\nИ все твои печали под чёрною водой')

        speak('\nКто ты — горе или радость? То замерзнешь, то растаешь'
              '\nКто ты — ласковое солнце или мёртвый белый снег?'
              '\nЯ понять тебя пытаюсь, кто же ты на самом деле'
              '\nКто же ты на самом деле, айсберг или человек?')

        speak('\nА я про всё на свете с тобою забываю'
              '\nА я в любовь, как в море, бросаюсь с головой'
              '\nА ты такой холодный как айсберг в океане'
              '\nИ все твои печали под чёрною водой'
              '\nИ все твои печали под чёрною водой')

        speak('\nТы уйди с моей дороги или стань моей судьбою'
              '\nПротяни навстречу руки и поверить помоги'
              '\nЧто любовь моя сумеет примирить меня с тобою'
              '\nИ растает этот айсберг, это сердце без любви')

        speak('\nА я про всё на свете с тобою забываю'
              '\nА я в любовь, как в море, бросаюсь с головой'
              '\nА ты такой холодный как айсберг в океане'
              '\nИ все твои печали под чёрною водой'
              '\nИ все твои печали под чёрною водой')

        time.sleep(15)

        mixer.music.stop()


name = 'Сашка'

# Для функционала
owm = pyowm.OWM('6f5dc1652adf891c89bf794c92ff3ba4')
mgr = owm.weather_manager()

place = 'Санкт-Петербург'

config_dict = get_default_config()
config_dict['language'] = 'ru'

observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')['temp']
cloud = w.detailed_status

# Для приколов
mistakes = -2

# Основной цикл
while True:
    command(makeSomething())
