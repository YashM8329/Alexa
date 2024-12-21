# Importing libraries
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

# Initializing and Setting Parameters
engine = pyttsx3.init()
listener = sr.Recognizer()
wikipedia.set_lang('en')


# Function to talk back
def talk(text):
    engine.say(text)
    engine.runAndWait()


# Function to listen to what you say
def listen():
    command = ""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_sphinx(voice)
            engine.say(command)
            engine.runAndWait()
            print(command)

    except Exception as e:
        print("error", e)

    return command

def whatsapp():
    pywhatkit.sendwhatmsg("+916356503394", "Hi", 22, 56)
    return print("Message sent!")


# Function to get manual text input
def get_text_input():
    print("Type your command:")
    return input()


# Function to make laptop do some task
def task(command):
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'what is' in command or 'how is' in command or 'who is' in command or 'why is' in command:
        search = command.split('is ', 1)[1] if 'is ' in command else command
        page = wikipedia.page(search)
        print("Title: ", page.title)
        print("Content: ", page.content[:100])
        talk(page.title)
        talk(page.content[:100])
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Come again')


# Main loop
while True:
    print("Press V to use voice command, T to type your command, W to whatsapp your msg:")
    choice = input().strip().upper()
    if choice == 'V':
        command = listen()
    elif choice == 'T':
        command = get_text_input()
    elif choice == 'W':
        command = whatsapp()
    else:
        print("Invalid choice. Try again.")
        continue

    task(command)
