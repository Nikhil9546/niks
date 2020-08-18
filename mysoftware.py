import pyttsx3
import os

print()
print('Press 1: to open chrome browser')
print('Press 2: to open notepad')
print('Press 3: to open media player')
print()

print("enter ur choice : " , end='')
p=input()

if int(p) == 1:
  os.system("chrome")

elif int(p) == 2:
  os.system("notepad")

elif int(p) == 3:
  os.system("wmplayer")

else:
  print("dont support")
