import pyttsx3

engine = pyttsx3.init()

engine.save_to_file('你好，中国!', 'test.mp3')
engine.runAndWait()