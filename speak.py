#!/usr/bin/env python3
import bidi
import itertools
import pyttsx3
import random
import sys
import time

#  [ [i.languages, i.id] for i in n.voice.getProperty("voices") ] - retrieves languages
CURRENT_LANGUAGE_CODES = {
    "it_IT": "com.apple.speech.synthesis.voice.luca",  # Modern Standard Italian
    "el_GR": "com.apple.speech.synthesis.voice.melina",  # Modern Standard Greek
    "fr_FR": "com.apple.speech.synthesis.voice.thomas", # Parisian French
    "fr_CA": "com.apple.speech.synthesis.voice.amelie",  # Canadian French
    "de_DE": "com.apple.speech.synthesis.voice.anna",  # Hochdeutsch
    "he_IL": "com.apple.speech.synthesis.voice.carmit",  # Israeli Hebrew

} 

class Narrator:
    def __init__(self, language_code=None):
        self.voice = pyttsx3.init()
        if language_code:
            self.set_language(language_code)
    
    @classmethod
    def lookup_voice_id(cls, language_code):
        return CURRENT_LANGUAGE_CODES[language_code]

    def set_language(self, language_code):
        voice_id = self.lookup_voice_id(language_code)
        self.voice.setProperty("voice", voice_id)

    def speak(self, text):
        fmt_text = f"{text}"
        self.voice.say(fmt_text)
        self.voice.runAndWait()

def main():
    narrator = Narrator("he_IL")
    while True:
        user_input = input("> ")
        narrator.speak(user_input)
        if user_input == "q":
            sys.exit(0)


if __name__ == "__main__":
    main()
