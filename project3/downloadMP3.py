import urllib.request
import vlc

path = "http://files.cessor.de/"
filename = "Stainless-NotAJedi.mp3"

print('downloading...')
#urllib.request.urlretrieve (path+filename, filename)
print('download complete.')
player = vlc.MediaPlayer(filename)
print('playing file...')
player.play()
print('all done.')