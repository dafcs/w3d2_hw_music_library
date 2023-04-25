from db.run_sql import run_sql
from models.album import Album
from models.artist import Artist
import repositories.artist_repo


# CRUD

# Create
def save(album):
    sql = f'INSERT INTO'
