import PIL
import os
import datetime 
import time
from PIL import ImageGrab

TargetFolder = r"C:\Screenshots"
CurrentImage = None
ImageGrabberEnabled = True
FileName = "FirstScreenie.png"

if os.path.exists(TargetFolder):
    print(f"Target folder found : {TargetFolder}")
else:
    os.mkdir(TargetFolder)
    print(f"Created Missing Folder : {TargetFolder}")

if ImageGrabberEnabled == True:
    CurrentImage = ImageGrab.grab()
    FullPath = os.path.join(TargetFolder, FileName)
    File = CurrentImage.save(FullPath)
    print(f"Took Screenshot : Saved to {TargetFolder}")

