from gtts import gTTS

language="en"
text1="Hello Word, I am sentient machine!"

speech=gTTS(text=text1, lang=language, slow=False,tld="com.au")
speech.save("textToSpeech.mp3")