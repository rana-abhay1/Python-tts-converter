import os
# import pyttsx3

print("Hello !!!\nThis is a text to speech converter.\n press 'q' to quit the program.\n")


while True:    
    x = input("Enter the text you want to convert to speech: \n ->")
    
    if x == "q":
        print("Goodbye!")
        break
    
    command = f"PowerShell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}');\""
    os.system(command)
    


#  Alternative method using pyttsx3 library


# engine = pyttsx3.init()

# while True:
#     x = input("Enter the text you want to convert to speech (or q to quit): \n ->").strip()
#     if x.lower() == "q":
#         print("Goodbye!")
#         break

#     engine.say(x)
#     engine.runAndWait()
