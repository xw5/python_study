import pyttsx3

def textToAudio(text, name):
    engine = pyttsx3.init()
    # rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    # volume = engine.getProperty('volume')
    engine.setProperty('volume', 1.0)
    engine.save_to_file(text, '{}.mp3'.format(name))
    engine.runAndWait()