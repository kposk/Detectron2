from detector import *
import os
import cv2

detec = Detector()


print("Choose the file you want to detect:\n")
print(f'1: Video\n'
       '2: Image\n')
print("Type here: ", end="")
choice = int(input())


if choice == 1:
    print("VIDEO FULL PATH: ", end="")
    videoPath = input()

    detec.onVideo(videoPath)

elif choice == 2:

    print("IMAGE FULL PATH: ", end="")
    imagePath = input()
    
    detec.onImage(imagePath)

else:
    exit(1)



