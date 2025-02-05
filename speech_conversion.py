from gtts import gTTS
from speech_recognition_voice import recognize_speech_from_mic
import io
from pydub import AudioSegment
from pydub.playback import play

def speak_command(com_text):
    print(com_text)
    if com_text == "открой браузер":
        text = "Скажите код доступа"

    elif com_text != "1804":
        text = "Доступ запрещён"

    tts = gTTS(text, lang="ru")
    audio_stream = io.BytesIO()
    tts.write_to_fp(audio_stream)
    audio_stream.seek(0)

    audio = AudioSegment.from_file(audio_stream, bormat="mp3")

    play(audio)





