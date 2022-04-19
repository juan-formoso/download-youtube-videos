from pytube import YouTube
link = input("Enter url / Digite o link: ")
yt = YouTube(link)
stream = yt.streams.get_highest_resolution()
stream.download()