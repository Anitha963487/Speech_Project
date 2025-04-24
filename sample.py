import pyttsx3
import speech_recognition as sr
import webbrowser
import otp

def speak(text):
  engine = pyttsx3.init()
  voices = engine.getProperty('voices')
  engine.setProperty('voice',voices[1].id)
  engine.say(text)
  engine.runAndWait() 
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak to recognize.....")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing......")
            query = r.recognize_google(audio,language="en-in")
            print(query)
        except:
            print("Speak Again")
            return False
        else:
            return query
def greet():
    greeting = "Hello, How can i help You ?"
    speak(greeting)
greet()
while True:
    query = takecommand()
    if query == False:
        pass
    elif "how are you" in query.lower():
        speak("I am doing Good, How about you !")
    elif "shut down" in query.lower():
        speak("Take Care, Bye !")
        break
    elif "open web page" in query.lower():
        speak("Opening Codegnan Website !")
        webbrowser.open("www.codegnan.com")
    elif "open flipkart" in query:
        speak("Opening Flipkart website!")
        webbrowser.open("https://www.flipkart.com")
    elif "open amazon" in query:
        speak("Opening Amazon wbesite!")
        webbrowser.open("https://www.amazon.in")
    elif "send otp" in query.lower():
        speak("Enter Email address: ")
        x = input("Enter email here: ")
        otp.otp(x)
        speak("Otp Sent Sucessfully")
    else:
        speak("Sorry,I don't understand that command.")
if _name__ == "__main__":
    main()
