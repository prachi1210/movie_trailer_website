import webbrowser

class Movie():
    def __init__(self, movie_title, poster_image,trailer):
        self.title=movie_title
        self.poster=poster_image
        self.trailer_url=trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
