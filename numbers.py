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
        self.voice.say(fmt_text)
        self.voice.runAndWait()

def generate_cardinal_numbers(rng, len):
    return [random.randrange(0, rng) for i in range(rng)]

def cardinal_numbers(rng=11, len=9):
    drill = generate_cardinal_numbers(rng, len)
    return f'{drill}'

def main():
    turn = 1
    narrator = Narrator("he_IL")
    nxt = True
    while True:
        if nxt:
            intro = f"תרגיל מספר {turn}."
            print(intro)
            narrator.speak(intro)
            drill = cardinal_numbers()
            nxt = False

        narrator.speak(drill)

        if "r" == input():
            continue
        elif "v" == input():
            print(drill)
        elif "q" == input():
            print(drill)
            sys.exit(0)
        elif "n" == input():
            turn += 1
            nxt = True
        time.sleep(0.001)


if __name__ == "__main__":
    main()
