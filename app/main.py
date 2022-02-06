import pytube

# link = input('Veuillez entrer un lien YouTube : ')
link = 'https://www.youtube.com/watch?v=0vJoRP6_5tI'

yt = pytube.YouTube(link)

# Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print(f"Length of video: {yt.length}s")


stream = yt.streams.get_highest_resolution()
print('Donwloading...')

stream.download()
print('Donwload complete')