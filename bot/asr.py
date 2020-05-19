import speech_recognition as sr

def asr(device_id: int) -> str:
    sample_rate = 48000
    chunk_size = 2048
    r = sr.Recognizer()

    with sr.Microphone(device_index = device_id, sample_rate = sample_rate,
                            chunk_size = chunk_size) as source:
        #wait for a second to let the recognizer adjust the
        #energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source)
        print("Say Something")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("you said: " + text)
            return text

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")

        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

def list_mics():
    mic_list = sr.Microphone.list_microphone_names()
    return mic_list
