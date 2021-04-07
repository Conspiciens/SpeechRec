# 1 -> Introduction
# 2 -> Questions
# 3 -> Answers

import pyttsx3
import speech_recognition as sr
import wolframalpha
import wikipedia
import json

from Leon.lists import the_lists
from Leon.lists import listening_command
from Leon.lists import open_file_read

engine = pyttsx3.init('nsss')
client = wolframalpha.Client('GJP9EQ-9Y6KH49TE3')


def introduction():
    engine.say("Hello, How may I help you today")
    engine.runAndWait()
    engine.stop()


def if_statements(study_input):
    getobject = the_lists(study_input)

    name = getobject.search_for_introduction()
    print(name)


def main():
    introduction()
    if_statements(listening_command())


if __name__ == '__main__':
    main()