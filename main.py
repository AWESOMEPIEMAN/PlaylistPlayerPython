from playsound import playsound

import glob

def playlist(path):
    for song in glob.glob(path):
        print("Now Playing : " + song)
        playsound(song)

playlist("C:/*.mp3") #yourpath
