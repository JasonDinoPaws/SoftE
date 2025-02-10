from pydub import AudioSegment
from pydub.playback import play
from os import listdir
from time import sleep
path = "Sounds"

soundnames = []
sounds = []

try:
    listdir(path)
except:
    path = "Hat kid ai/"+path

for s in listdir(path):
    soundnames.append(s.split(".")[0].lower())
    sounds.append(AudioSegment.from_file(f"{path}/{s}"))

def GetSound(name:str):
    name  = name.lower()
    if name in soundnames:
        return sounds[soundnames.index(name)]
    return False

def Playsound(name):
    print(name)
    sound = GetSound(name)
    if sound:
        play(sound)
        sleep(.05)

def GetAvaliableSounds():
    return soundnames
