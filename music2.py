import music21 as music
from pysine import sine
import time

c = music.note.Note("C5").pitch.frequency
d = music.note.Note("D5").pitch.frequency
e = music.note.Note("E5").pitch.frequency
f = music.note.Note("F5").pitch.frequency
g = music.note.Note("G5").pitch.frequency
a = music.note.Note("A5").pitch.frequency
b = music.note.Note("B5").pitch.frequency

def Birthday():
    sine(frequency=c, duration=0.25)
    sine(frequency=c, duration=0.25)
    sine(frequency=d, duration=0.5)
    sine(frequency=c, duration=0.5)
    sine(frequency=f, duration=0.5)
    sine(frequency=e, duration=0.5)

def Mary():
    sine(frequency=e, duration=0.25)
    sine(frequency=d, duration=0.25)
    sine(frequency=c, duration=0.25)
    sine(frequency=d, duration=0.25)
    sine(frequency=e, duration=0.25)
    sine(frequency=e, duration=0.25)
    sine(frequency=e, duration=0.25)
    

while True:
    #conditionals
    song = input("What notes would you like me to play?")

    for i in song:
        print(i)
        match i:
            case "C":
                sine(frequency=c, duration=0.3)
            case "D":
                sine(frequency=d, duration=0.3)
            case "E":
                sine(frequency=e, duration=0.3)
            case "F":
                sine(frequency=f, duration=0.3)
            case "G":
                sine(frequency=g, duration=0.3)
            case "A":
                sine(frequency=a, duration=0.3)
            case "B":
                sine(frequency=b, duration=0.3)
            case _:
                print("Sorry! That wasn't an option. Run the program again.")

    
    
