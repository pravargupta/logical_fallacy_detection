import speech_recognition as sr
from prompt import main

r = sr.Recognizer()

def record_audio():
    with sr.Microphone() as source2:
        print("Listening...")
        audio2 = r.listen(source2)
        print("Finished listening.")
    return audio2

def output_text(text):
    with open("output.txt", "a") as f:
        f.write(text + "\n")
    f.close()

def real_time_with_microphone():
    f = open("output.txt", "w")
    f.truncate(0)
    f.close()
    try:
        while True:
            audio = record_audio()
            try:
                text = r.recognize_google(audio)
                output_text(text)
                print("Wrote text:", text)
                if text.lower() == "exit":
                    break
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand the audio")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting gracefully.")
    main()

real_time_with_microphone()
