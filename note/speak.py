import speech_recognition as sr

from gtts import gTTS

import os

import time

import playsound

'''
안녕하세요. 길동씨라고 읽어주는 결과를 맞이할 것이다.

먼저 pip install speechrecognition 실행

pip install gTTs 실행

그리고 마지막으로 pip install playsound 실행

3가지는 기본으로 설치되어야 실행이 된다는 사실은 기억하자.

실행후 작업폴더에 보면 voice.mp3로 저장된 파일을 만날 수 있다.

너무도 신통방통한 음성으로 읽어주는 TTS 이제 어렵지 않게 접근할 수 있다
'''

def speak( text ):

    tts = gTTS( text=text, lang='en' )

    filename = 'voice.mp3'

    tts.save( filename )

    playsound.playsound( filename )
    os.remove( filename )


warning = 'Warning, Hannah needs more chocolates.'
alert = 'Beep Beep, Hannah is hungry'

speak( warning )
speak( alert )



