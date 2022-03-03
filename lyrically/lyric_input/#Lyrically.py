#Lyrically

lyrics = []

def add_lyric():
    new_lyric = input ("Add new lyrics: ")
    if new_lyric in lyrics:
        print ("This song is already in my system, please try again.")
        return
    else:
        lyrics.append(new_lyric)

print (add_lyric())
