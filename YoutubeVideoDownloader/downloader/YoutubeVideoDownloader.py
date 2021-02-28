#Youtube Video Downloader Python Code
#Made By Rushil Desai
def youtubeVideo(link, path, name, aud, prog, res):
    #Imports 
    from pytube import YouTube
    import os.path
    
    #Youtube Video Object Creation
    try:
        video = YouTube(link)
    except Exception as exc:
        return("Error: Video could not be recognized\n" + exc)
    
    #Streams Initialization
    allStreams = video.streams
    print("\nAll Streams:\n")
    for stream in allStreams:
        print(stream)

    #Audio Selection
    if (aud == "true"):
        try:
            filterStreams = allStreams.get_audio_only()
        except Exception as exc:
            return("Error: Video does not support audio only\n" + exc)
    elif (aud == "false"):
        try:
            filterStreams = allStreams.filter(file_extension = "mp4")
        except Exception as exc:
            return("Error: Video does not support audio and video\n" + exc)
    
    #Progressive Selection
    if (prog == "true"):
        try:
            filterStreams = filterStreams.filter(progressive = True)
        except Exception as exc:
            return("Error: Video does not support Progressive downloading\n" + exc)
    elif (prog == "false"):
        try:
            filterStreams = filterStreams.filter(progressive = False)
        except Exception as exc:
            return("Error: Video does not support Adaptive downloading\n" + exc)

    #Resolution Selection
    if (res == "true"):
        bestStream = filterStreams.get_highest_resolution()
    elif (res == "false"):
        bestStream = filterStreams.get_lowest_resolution()

    #Exporting Chosen Stream
    print("\nChosen Stream:")
    print(bestStream)
    bestStream.download(output_path = path, filename = name)

#youtubeVideo("Insert Link","Insert Path", "Insert Name", "false or true", "true or false", "true or false")
