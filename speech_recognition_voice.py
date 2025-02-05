import speech_recognition as sr

def recognize_speech_from_mic():
    mic =  sr.Microphone(device_index=1)
    r = sr.Recognizer()
    r.pause_threshold = 1
    with mic as sourse:
        print("Говорите")
        audio = r.listen(sourse)

    try:
        cho = r.recognize_google(audio_data=audio, language="ru-RU")
        return cho

    except sr.UnknownValueError:
        return "хз чо сказал"

    except sr.WaitTimeoutError:
        return "сеть хуня"

#while True:
#    print(recognize_speech_from_mic())
