# 1 -> Introduction
# 2 -> Questions
# 3 -> Answers

import pyttsx3
import speech_recognition as sr
import wikipedia
import json

from lists import the_lists
from lists import listening_command
from lists import open_file_read

r = sr.Recognizer()

def input_sound_file(name_file): 
    recording = sr.AudioFile(name_file)
    for reord in recording: 
        audio = r.record(source)

    r.recognize_google(audio)




if __name__ == '__main__':
    