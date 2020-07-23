from gtts import gTTS
mytext = "Machine learning with python is a one month training camp organised by SRFGSS and Robokalam"
language = 'en'
my_conversion = gTTS(text=mytext,lang=language,slow=False)
my_conversion.save('myaudio.mp3')
