import speech_recognition as sr
from turtle import *
import data

program_is_running = True  

color('red', 'yellow')
begin_fill()
left(90)

r = sr.Recognizer()

def checking_word(text):

    global program_is_running

    text_arr = text.split(" ")
    
    for word in text_arr:
        if word in data.ending_words:
            program_is_running = False
            end_fill()
            done()
        elif word in data.right_words: 
            forward(10)
            right(10)
        elif word in data.left_words:
            forward(10)
            left(10)                 
        
while program_is_running:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Talk")
        audio_text = r.listen(source)

        try:
            recognized_text = r.recognize_google(audio_text, language=data.PROGRAM_LANGUAGE)
            print("Text: "+recognized_text)
            checking_word(recognized_text)

        except:
            print("Sorry, I did not get that")

