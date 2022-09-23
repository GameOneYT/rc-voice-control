#import library
import data
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)

r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable
    

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Talk")
    audio_text = r.listen(source)
    
    try:
        # using google speech recognition
        output_text = r.recognize_google(audio_text)
        print("Text: "+ output_text)
    except:
         print("Sorry, I did not get that")
         
    if "hello" in output_text:
        print("Hellollllfvkjdfnkvjfd")
        
    if output_text in data.front:
        print("frontt")
