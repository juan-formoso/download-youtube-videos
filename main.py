from pytube import Youtube
link = input("Enter url / Digite o link: ")
yt = Youtube(link)
stream = yt.streams.get_highest_resolution()
stream.download()