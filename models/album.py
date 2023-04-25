class Album():
    def __init__(self,title,genre,artist,id=None):
        self.title = title
        self.genre = genre
        self.artist = artist
        self.id = id

# ID set to none as this is assigned by the db once saved
