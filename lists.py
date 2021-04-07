import wikipedia
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()


class the_lists:
    def __init__(self, get_line):
        self.get_line = get_line

    def search_for_introduction(self):
        num = 2

        for line in open_file_read():
            line.replace("\n", "")
            print("Here One " + line + "\n")
            if line.find(str(num)):
                line.replace("\n", "")
                print("Here " + line + "\n")
                if self.get_line.find(str(line)) != -1:
                    l, s = line.split(self.get_line)
                    print(str(s))
                    return s
            else:
                print("Unable to find the question, add it to your question list?")

    def insert_list(self):
        engine.say("What would you like to add Sir?")

        f = open('questions.txt', 'w')
        f.write(self.get_line)


def listening_command():
    k = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        k.pause_threshold = 1
        audio = k.listen(source)

    try:
        Input = k.recognize_google(audio, language='en')
        print('Got it: ' + Input + '\n')

    except sr.UnknownValueError:
        engine.say("Sorry I wasn't able to understand what you were saying")
        Input = str(input('Command: '))

    return Input


def open_file_read():
    file = open('questions.txt', 'r')
    l = file.readlines()
    print(l)
    return l


def open_file_write():
    return open('questions.txt', 'w')