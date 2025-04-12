import music21 as music
from pysine import sine

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
    song = input("What song would you like me to play?")

    if song == "Happy Birthday":
        Birthday()
    elif song == "Mary Had a Little Lamb":
        Mary()
    else:
        print("Sorry! That wasn't an option. Run the program again.")

    
    
