import speech_recognition as sr
import json

r = sr.Recognizer()

def input_sound_file(name_file): 
    recording = sr.AudioFile(name_file)
    with recording as record: 
        audio = r.record(record)

    # AI used to get the audio
    text = r.recognize_google(audio)
    return text


def TierOneCheck(text, commands):
    with open("grade_command.json") as grade: 
        gr = json.load(grade)

        # goes through the tiers to see where command should be located
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

if __name__ == '__main__':
    with open("check_commands.json") as commands: 
        text = input_sound_file("read.wav")
        js = json.load(commands)
        TierOneCheck(text.lower(), js)
