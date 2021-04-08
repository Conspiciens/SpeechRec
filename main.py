# 1 -> Introduction
# 2 -> Questions
# 3 -> Answers

import speech_recognition as sr
import json
import threading

# from lists import the_lists
# from lists import listening_command
# from lists import open_file_read

r = sr.Recognizer()

def input_sound_file(name_file): 
    recording = sr.AudioFile(name_file)
    with recording as record: 
        audio = r.record(record)

    text = r.recognize_google(audio)
    return text
    # important_commands(text)


def TierOneCheck(text, commands):
    with open("grade_command.json") as grade: 
        gr = json.load(grade)

        for command in commands["TierOne"]: 
            if text.find(command) != -1: 
                gr["High"].append({
                    "C" : str(text)
                })
                
                write_file(gr)

        for command in commands["TierTwo"]: 
            if text.find(command) != -1: 
                gr["Medium"].append({
                    "C": str(text)
                })
                write_file(gr)

        for command in commands["TierThree"]: 
            if text.find(command) != -1: 
                gr["Low"].append({
                    "C": str(text)
                })
                write_file(gr)

def write_file(gr):
    with open('grade_command.json', 'w') as outfile:
        json.dump(gr, outfile, indent=4)

'''def important_commands(text):
    with open("check_commands.json") as check_com: 
       list_command = json.load(check_com)

        for command in list_command["TierOne"]: 
            print(command)

        for command in list_command["TierTwo"]:
            print(command)

        for command in list_command["TierThree"]: 
            print(command)   
'''



if __name__ == '__main__':
    with open("check_commands.json") as commands: 
        text = input_sound_file("read.wav")
        js = json.load(commands)
        TierOneCheck(text.lower(), js)


        # t1 = threading.Thread(target=TierOneCheck(text, js))
        # t2 = threading.Thread(target=TierTwoCheck(text, js))
        # t3 = threading.Thread(target=TierThreeCheck(text, js))

        # t1.start()
        # t1.join()
        # t2.start()
        # t2.join()
        # t3.start()
        # t3.join()

        # important_commands("Helo", commands)