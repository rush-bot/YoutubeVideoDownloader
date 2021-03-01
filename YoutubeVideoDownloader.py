#Youtube Video Downloader Python Code
#Made By Rushil Desai

#Imports
from pytube import YouTube
import os.path
import os

#Initialization
print("Welcome to the Youtube Video Downloader!\nThe fastest and easiest way to download a youtube video.")
print("Lets start off by typing in the link to the video below.")
link  = input()

#Youtube Video Object Creation
val = False
while val == False:
    try:
        video = YouTube(link)
        val = True
    except:
        print("Error: Video could not be recognized. Try inputting a different link.")

#Streams Initialization
allStreams = video.streams
print("\nHere are all the possible download types of your chosen Youtube Video:\n")
for stream in allStreams:
    print(stream)

#Audio Selection
print("The next step is choose an audio type.\nType in true for Audio and Video or false for Audio Only")
while True:
    aud = input()
    if (aud == "true" or aud == "TRUE" or aud == "True"):
        try:
            filterStreams = allStreams.filter(file_extension = "mp4")
            break
        except:
            print("Error: Video does not support audio and video\n")  
            continue

    elif (aud == "false"):
        try:
            filterStreams = allStreams.get_audio_only()
            break
        except:
            print("Error: Video does not support audio only\n")
            continue
    else:
        print("Type in either true or false.")
        continue

#Progressive Selection
print("Next, you will need to choose the download type.\nType in true for a Progressive Download or false for an Adaptive Download.")
while True:
    down = input()
    if (down == "true" or down == "TRUE" or down == "True"):
        try:
            filterStreams = filterStreams.filter(progressive = True)
            break
        except:
            print("Error: Video does not support Progressive downloading\n")
            continue

    elif (down == "false" or down == "FALSE" or down == "False"):
        try:
            filterStreams = filterStreams.filter(progressive = False)
            break
        except:
            print("Error: Video does not support Adaptive downloading\n")
            continue
    else:
        print("Type in either true or false.")
        continue

#Resolution Selection
print("Almost Done! Type true for high resolution or false for low resolution.")
res = input()
if (res == "true" or res == "TRUE" or res == "True"):
        bestStream = filterStreams.get_highest_resolution()
elif (res == "false" or res == "FALSE" or res == "False"):
        bestStream = filterStreams.get_lowest_resolution()

#Video Data and Export
print("Last step!")
while True:
    try:
        print("What do you want the video to be named?")
        name = input()
        print("Type in the exact file path of where you want the video to be saved.")
        path = input()
        bestStream.download(output_path = path, filename = name)
        break
    except:
        print("There was an error in downloading. Try typing in another file nae and path.")
        continue

#Final Output
print("\nThe download was Successful! Here is your chosen download:")
print(bestStream)
    