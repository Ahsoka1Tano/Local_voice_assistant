import subprocess
import webbrowser
import os
from speech_conversion import speak_command
from speech_recognition_voice import recognize_speech_from_mic

def command():
    text = recognize_speech_from_mic().lower()
    com = "открой браузер"
    print(text)

    if com in text:
        speak_command(com)
        code = recognize_speech_from_mic()
        if code == "1804":
            subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe", shell=True)
        else:
            print(type(code))
            speak_command(code)

command()