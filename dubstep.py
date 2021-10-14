def song_decoder(song):
    result = [word for word in song.split("WUB") if word != ""]
    return ' '.join(result)