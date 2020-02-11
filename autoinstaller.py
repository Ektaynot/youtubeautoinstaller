import os
print("Welcome To The AutoVideoİnstaller.")
link=input("Please Paste Your Link:")
os.system("youtube-dl -F '"+link+"'")
vidnumber=input("Please Write The Number For Video Input:")
vidcodec=input("Please Select Your Videos Codec 1(webm) or 2(mp4)")
audionumber=input("Please Write The Number For Audio Input:")
audiocodec=input("Please Select Your Videos Codec 1(webm) or 2(m4a)")
name=input("What Is Your Videos Name:")
if vidcodec == "1":
    os.system("youtube-dl -o 'video.webm' -f "+vidnumber+" '"+link+"'")
    if audiocodec == "2":
        os.system("youtube-dl -o 'audio.m4a' -f "+audionumber+" '"+link+"'")
        os.system("ffmpeg -i video.webm -i audio.m4a -c copy "+name+".mkv")
        os.system("rm video.webm")
        os.system("rm audio.m4a")
    elif audiocodec == "1":
        os.system("youtube-dl -o 'audio.webm' -f "+audionumber+" '"+link+"'")
        os.system("ffmpeg -i video.webm -i audio.webm -c copy "+name+".mkv")
        os.system("rm video.webm")
        os.system("rm audio.webm")
    else:
        raise SystemExit
elif vidcodec == "2":
    os.system("youtube-dl -o 'video.mp4' -f "+vidnumber+" '"+link+"'")
    if audiocodec == "2":
        os.system("youtube-dl -o 'audio.m4a' -f "+audionumber+" '"+link+"'")
        os.system("ffmpeg -i video.mp4 -i audio.m4a -c copy "+name+".mkv")
        os.system("rm video.mp4")
        os.system("rm audio.m4a")
    elif audiocodec == "1":
        os.system("youtube-dl -o 'audio.webm' -f "+audionumber+" '"+link+"'")
        os.system("ffmpeg -i video.mp4 -i audio.webm -c copy "+name+".mkv")
        os.system("rm video.mp4")
        os.system("rm audio.webm")  
    else:
        raise SystemExit
