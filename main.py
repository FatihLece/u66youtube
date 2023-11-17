import pytube

url = input("enter video url: ")
path = ""  # if used "" then video will be saved as the same folder as udemy66 folder.

pytube.YouTube(url).streams.get_lowest_resolution().download(path)
