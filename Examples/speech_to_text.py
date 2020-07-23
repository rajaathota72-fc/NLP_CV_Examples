import speech_recognition as sr
r = sr.Recognizer()
#### without microphone
#with sr.AudioFile('sample.wav') as source:
    #audio_text = r.listen(source)
    #text = r.recognize_google(audio_text)
    #print(text)
#### with microphone
with sr.Microphone() as source:
    print("talk")
    audio_text = r.listen(source)
    text = r.recognize_google(audio_text)
    print(text)

