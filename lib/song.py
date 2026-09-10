class Song:
    # Class attributes - shared across every Song instance
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes - unique to each song
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update all class-level tracking whenever a new song is created
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()

    def add_song_to_count(self):
        """Increment the running total of Song instances created."""
        Song.count += 1

    def add_to_genres(self):
        """Add this song's genre to the class-level genres list, keeping entries unique."""
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)

    def add_to_artists(self):
        """Add this song's artist to the class-level artists list, keeping entries unique."""
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)

    def add_to_genre_count(self):
        """Increment this genre's tally in genre_count, initializing it to 1 if new."""
        if self.genre in Song.genre_count:
            Song.genre_count[self.genre] += 1
        else:
            Song.genre_count[self.genre] = 1

    def add_to_artist_count(self):
        """Increment this artist's tally in artist_count, initializing it to 1 if new."""
        if self.artist in Song.artist_count:
            Song.artist_count[self.artist] += 1
        else:
            Song.artist_count[self.artist] = 1