import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes



# Initialize the recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()


#Set female voice 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #1 for female 

def talk(text) :
    # Convert text to speech
    print("ELSA:", text)
    engine.say(text)
    engine.runAndWait() 


def take_command() :
    # Listen to user's voice and recognize the command
    command = ""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'ELSA' in command:
                command = command.replace('ELSA', '')
                print("You siad:", command)
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
    except sr.RequestError:
        print("Network error. Check your internet connection.")
    return command

def run_alexa() :
    # Process the command and respond accordingly
    command = take_command()

    if 'play' in command:
        song = command.replace('play', '').strip()
        talk("Playing" + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("The current time is " +time)
    
    elif 'who is' in command or 'who the heck is' in command:
        person = command.replace('who the heck is', '').replace('who is', '').strip()
        info = wikipedia.summary(person, 1)
        talk(info)

    elif 'date' in command:
        date = datetime.datetime.now().strftime('%A, %B %d, %Y')
        talk("Today's date is: " + date)
        
    elif 'are you single' in command:
        talk("I am in a relationship with Wifi")

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif command != "":
        talk("Please say the command again.")

    elif 'Thank you' in command:
        talk("You are welcome!")
    else:
        pass #No voice detected, ignore silently


# Run ELSA continuously
while True:
    run_alexa()