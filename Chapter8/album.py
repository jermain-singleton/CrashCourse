def make_album(artist_name, album_title, tracks=''):
    """Return a dictionary of artist name and title"""
    album = {'artist': artist_name, 'title': album_title}
    if tracks:
        album['tracks'] = tracks
    return album

while True:
    a_name = input("aritst name: ")
    if a_name == 'q':
        break
    a_title = input("album title: ")
    if a_title == 'q':
        break
    new_artist = make_album(a_name, a_title )
    print(new_artist)
