from models.album import Album
from models.artist import Artist
import repositories.album_repo as album_repo
import repositories.artist_repo as artist_repo

artist = Artist('Jon Bovi')
artist_repo.insert(artist)

result = artist_repo.select_all()
# for artist in result:
#     print(result)