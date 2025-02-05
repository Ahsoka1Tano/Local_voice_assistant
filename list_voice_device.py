import speech_recognition as sp

mic = sp.Microphone()
list_mic = sp.Microphone.list_microphone_names()

for i in range(0, len(list_mic)):
    print(i, list_mic[i])