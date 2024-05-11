# I am going to create a Robospeaker python program that will convert the text into speech .
''' To do that in window, well i am saying this because if you are in macos you can simply use its built in
    say command line for text-to-speech , but in window (The os.system("say hello") command works for macOS because macOS has
     a built-in "say" command for text-to-speech. However, Windows doesn't have a direct equivalent.
1. Using the pywin32 library it is a offline .:
This library allows you to interact with the Microsoft Speech API (SAPI) available on Windows systems.)'''

''' Steps-:
  1.install pywin32 package
  2.import the win32com.client package 
'''
# import win32com.client
from gtts import gTTS #importing gTTS module from gtts library.

# if __name__ == '__main__':
#     speak=win32com.client.Dispatch("SAPI.SpVoice")
#     while True:
#         command=input("enter your command to be spoken by Robo-: ")
#         if command=="0":
#             speak.Speak("Thank you for interacting with me sir ! see you soon")
#             break
#         speak.Speak(command)


'''
 Let's break down the code step by step:

import win32com.client: This line imports the client functionality from the win32com library. This library allows Python 
programs to interact with COM (Component Object Model) components available on Windows, including the Speech API.

speak = win32com.client.Dispatch("SAPI.SpVoice"): This line creates a new object called speak. It uses the Dispatch method 
from the imported client module. The argument "SAPI.SpVoice" instructs the Dispatch method to create an object that interacts
with the "SAPI.SpVoice" COM component. This component is the Microsoft Speech API responsible for text-to-speech conversion 
on Windows.

speak.Speak("Hello, this is text-to-speech from Python!"): This line utilizes the Speak method of the speak object. 
It passes the text string "Hello, this is text-to-speech from Python!" as an argument. This instructs the Speech API to 
convert the provided text to speech and play it through your computer's speakers.

In essence, this code snippet:

Imports the necessary library to interact with the Windows Speech API.
Creates an object to control the Speech API functionalities.
Uses the Speak method of the created object to convert a specific text string to spoken audio and play it.
'''

# Second method is to use the Google gtts library which is one of the text-to-speech popular method in python i had imported the libray at the starting after install it.-:
if __name__=='__main__':
    while True:
        text=input("enter the prompt to be played-:")
        if text=="0":
            text="Good day sir !"
            language="en"
            tts=gTTS(text=text,lang=language)
            tts.save("speech.mp3")
            import playsound
            playsound.playsound("speech.mp3")
            break
        # select you language
        language="en"
        # create object for gTTS
        tts=gTTS(text=text,lang=language)
        # save the audio as mp3 file
        tts.save("speech.mp3")
        import playsound
        # With this module, you can play a sound file with a single line of code:import playsound
        playsound.playsound("speech.mp3")

