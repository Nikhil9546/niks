import os
import pyttsx3

pyttsx3.speak("This app will help you to , open chrome , window media player , notepad , control panel , settings , and will also help you to shut down your computer , as well as restart your pc")
pyttsx3.speak("Text me your requirement Please")
while True:
    p=input("chat with me acc.to your requirements:")
    p=p.lower()
    if(("do not" not in p) and ("dont" not in p) and ("don't" not in p)) and ((("run" in p) or ("execute" in p) or ("open" in p)) and (("chrome" in p) or ("browser" in p) or ("search engine" in p) or ("google" in p))):
          os.system("chrome")
    elif(("do not" not in p) and ("dont" not in p) and ("don't" not in p)) and ((("run" in p) or ("execute" in p) or ("open" in p)) and (("player" in p) or ("window media player" in p) or ("audio player" in p) or ("video player" in p))):
          os.system("wmplayer")
    elif(("do not" not in p) and ("dont" not in p) and ("don't" not in p)) and ((("run" in p) or ("execute" in p) or ("open" in p)) and (("editor" in p) or ("notepad" in p) or ("text editor" in p) or ("writer" in p))):
          os.system("notepad")
    elif(("do not" not in p) and ("dont" not in p) and ("don't" not in p)) and ((("shutdown" in p) or ("turn off" in p) or ("close" in p) or ("off" in p)) and (("computer" in p) or ("pc" in p) or ("laptop" in p) or ("desktop" in p))):
          os.system("shutdown/s")
    elif(("do not" not in p) and ("dont" not in p) and ("don't" not in p)) and ((("restart" in p) or ("start again" in p) or ("close and start" in p) or ("shutdown and start again" in p)) and (("computer" in p) or ("pc" in p) or ("laptop" in p) or ("desktop" in p))):
          os.system("shutdown/r")
    elif(("do not" not in p) and ("dont" not in p) and ("don't" not in p)) and ((("open" in p) or ("run" in p) or ("execute" in p)) and (("control panel" in p) or ("hardware settings" in p) or ("software settings" in p) or ("user control settings" in p) or ("controlpanel" in p))):
          os.system("control panel")
    elif(("do not" not in p) and ("dont" not in p) and ("don't" not in p)) and ((("open" in p) or ("run" in p) or ("execute" in p)) and (("computer settings" in p) or ("settings" in p) or ("pc settings" in p))):
          os.system("start ms-settings:")
    elif("exit" in p) or ("close" in p) or ("quit" in p):
          break
    else:
          print("Try again !")
