from django.shortcuts import render
from django.http import HttpResponse
from downloader.models import video
import YoutubeVideoDownloader

def home(request):
    return render(request, "home.html")

def info(request):
    vid = video()
    vid.url = str(request.POST['Furl'])
    vid.name = str(request.POST['Fname'])
    vid.path = str(request.POST['Fpath'])
    vid.audio = str(request.POST['audio'])
    vid.download = str(request.POST['download'])
    vid.resolution = str(request.POST['resolution'])
    try:
        YoutubeVideoDownloader.youtubeVideo(vid.url, vid.path, vid.name, vid.audio, vid.download, vid.resolution)
        result = "The chosen video: " + vid.url + " has been downloaded!"
    except:
        result = "The chosen video: " + vid.url + " could not download."
    
    return render(request, "result.html", {'result':result})
