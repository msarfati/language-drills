#!/usr/bin/env python3
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
        print(fmt_text)
        self.voice.say(fmt_text)
        self.voice.runAndWait()

def generate_cardinal_numbers(rng, len):
    return [random.randrange(0, rng) for i in range(rng)]

def cardinal_numbers(turn, rng=11, len=9):
    drill = generate_cardinal_numbers(rng, len)
    return f'{turn}: {drill}'

def main():
    turn = 1
    narrator = Narrator("he_IL")
    while True:
        drill = cardinal_numbers(turn)
        narrator.speak(drill)
        if "q" == input():
            sys.exit(0)
        else:
            turn += 1
        time.sleep(0.1)


if __name__ == "__main__":
    main()
