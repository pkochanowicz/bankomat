import pyttsx3
import threading


class SynthSpeech():
    engine = None

    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 120)

    def start_synth_speech_thread(self, text):
        threading.Thread(
            target=SynthSpeech.pyttsx3_speech, args=(self, text,), daemon=True
        ).start()

    def pyttsx3_speech(self, text):
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except RuntimeError:
            pass
