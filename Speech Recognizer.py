import speech_recognition as sr

listener = sr.Recognizer()

def takecommand():
    try:
        with sr.Microphone as source:
            voice = listener.listen(source)
            query = listener.recognize_google(voice)
            query = query.lower

    except:
        pass
    return query
