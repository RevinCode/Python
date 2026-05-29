import PIL
import os
import keyboard
import random
import string
from PIL import ImageGrab

TargetFolder = r"C:\Screenshots"
CurrentImage = None
LetterPool = string.ascii_letters + string.digits

def Screenshot():
    if os.path.exists(TargetFolder):
        print(f"Target folder found : {TargetFolder}")
    else:
        os.mkdir(TargetFolder)
        print(f"Created Missing Folder : {TargetFolder}")

    RandString = "".join(random.choices(LetterPool, k=8))
    FileName = f"{RandString}.png"

    CurrentImage = ImageGrab.grab()
    FullPath = os.path.join(TargetFolder, FileName)
    File = CurrentImage.save(FullPath)
    print(f"Took Screenshot : Saved to {TargetFolder}")

keyboard.add_hotkey("shift+ctrl+s", Screenshot)

print("running")

keyboard.wait("esc")
