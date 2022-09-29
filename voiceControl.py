#import library
import data
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)

r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable
from turtle import *
color('green', 'yellow')
begin_fill()
speed(4)
# while True:
#     forward(250)
#     left(170)
#     forward(250)
#     right(201)
    
# end_fill()
# done()
# exit()
left(90)
last = 0 #for last function: 0 - nothin, 1 - forward, 2 - left, 3 - right, 4 - backward
def forwardd():
    global last
    last = 1
    forward(100)
    mainn()
    
def leftt():
    global last
    last = 2
    left(90)
    forward(100)
    right(90)
    mainn()
    
def rightt():
    global last
    last = 3
    right(90)
    forward(100)
    left(90)
    mainn()

def backk():
    global last
    last = 4
    right(180)
    forward(100)
    left(180)
    mainn()
    
def mainn():
    with sr.Microphone() as source:
        global output_text
        r.adjust_for_ambient_noise(source)
        print("Talk")
        audio_text = r.listen(source)

        try:
            # using google speech recognition
            output_text = r.recognize_google(audio_text)
            print("Text: " + output_text)
        except:
            print("Sorry, I did not get that")
            output_text = ""

        if output_text in data.forward:forwardd()
        elif output_text in data.left:leftt()    
        elif output_text in data.right:rightt()
        elif output_text in data.backward:backk()
        elif output_text in data.last:
            if last == 1: forwardd()
            elif last == 2: leftt()
            elif last == 3: rightt()
            elif last == 4: backk()
            mainn()
        elif output_text in data.stop: quit()
        else:
            print("Not recognized")
            mainn()

mainn()