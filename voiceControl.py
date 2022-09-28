import speech_recognition as sr
from turtle import *

program_is_running = True  

color('red', 'yellow')
begin_fill()
while program_is_running:
    right(10)
    forward(10)

ending_words = ["koniec", "wszystko", "end", "finish", "enough"]

PROGRAM_LANGUAGE = "en-UK"  # pl-PL

r = sr.Recognizer()

def checking_word(text):

    global program_is_running

    text_arr = text.split(" ")

    for word in text_arr:
        if word.lower() in ending_words:
            program_is_running = False
            end_fill()
            done()
        #data variables should be changed into 'word'_words, because turtle library has functions like right(), left(), forward()
        # elif word in right_words: 
        #     return "Rigth"
        # elif word in left_words:
        #     return "Left"
        # elif word in front_words:
        #     return "Front"
        # else: return "Nothing"


while program_is_running:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Talk")
        audio_text = r.listen(source)

        try:
            recognized_text = r.recognize_google(audio_text, language=PROGRAM_LANGUAGE)
            print("Text: "+recognized_text)
            checking_word(recognized_text)

        except:
            print("Sorry, I did not get that")
