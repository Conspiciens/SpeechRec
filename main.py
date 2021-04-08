# 1 -> Introduction
# 2 -> Questions
# 3 -> Answers

import pyttsx3
import speech_recognition as sr
import wikipedia
import json

# from lists import the_lists
# from lists import listening_command
# from lists import open_file_read

r = sr.Recognizer()

def input_sound_file(name_file): 
    recording = sr.AudioFile(name_file)
    with recording as record: 
        audio = r.record(record)

    print(r.recognize_google(audio))




if __name__ == '__main__':
    input_sound_file("read.wav")