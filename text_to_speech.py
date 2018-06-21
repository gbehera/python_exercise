from gtts import gTTS
import os

my_text = 'Hello I am a Patbot. Please give me some command.'

language = 'en'

obj = gTTS(text = my_text, lang = language, slow = False)

obj.save("welcome.mp3")

os.system("mpg321 welcome.mp3")