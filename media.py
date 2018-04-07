class Movie():
    """Class that contains details about a movie.

    Args:
        title (str): Title of the movie
        storyline (str): Short summary of movie's story
        poster_image_url (str): URL that links to poster image (100x100 pixels)
        trailer_youtube_url (str): URL that links to movie's trailer

    """

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
